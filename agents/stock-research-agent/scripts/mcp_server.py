#!/usr/bin/env python3
"""
Stock Research MCP Server
Exposes stock research tools via Model Context Protocol (MCP).

Usage:
    python mcp_server.py

This server provides the following tools:
- fetch_stock_data: Get comprehensive financial data
- run_dcf: Calculate intrinsic value via DCF
- compare_stocks: Compare multiple stocks
- get_sec_filings: Fetch SEC EDGAR filings
- get_news: Fetch recent news
- get_analyst_ratings: Get analyst recommendations

To use with Claude Code, add to ~/.claude/mcp_servers.json:
{
  "stock-research": {
    "command": "python3",
    "args": ["/path/to/stock-research-agent/scripts/mcp_server.py"]
  }
}
"""

import asyncio
import json
import sys
from typing import Any

# MCP protocol implementation
class MCPServer:
    """Simple MCP server implementation."""

    def __init__(self):
        self.tools = {
            "fetch_stock_data": {
                "description": "Fetch comprehensive financial data for a stock ticker including price, valuation, financials, and dividends.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "ticker": {
                            "type": "string",
                            "description": "Stock ticker symbol (e.g., AAPL, GOLF, MSFT)"
                        }
                    },
                    "required": ["ticker"]
                }
            },
            "run_dcf": {
                "description": "Run a DCF (Discounted Cash Flow) valuation model for a stock to calculate intrinsic value.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "ticker": {
                            "type": "string",
                            "description": "Stock ticker symbol"
                        },
                        "wacc": {
                            "type": "number",
                            "description": "Weighted Average Cost of Capital (default: 0.09 = 9%)"
                        },
                        "terminal_growth": {
                            "type": "number",
                            "description": "Terminal growth rate (default: 0.025 = 2.5%)"
                        }
                    },
                    "required": ["ticker"]
                }
            },
            "compare_stocks": {
                "description": "Compare two or more stocks side by side on valuation, financials, and returns.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "tickers": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of stock ticker symbols to compare"
                        }
                    },
                    "required": ["tickers"]
                }
            },
            "get_sec_filings": {
                "description": "Fetch SEC EDGAR filings (10-K, 10-Q, 8-K, etc.) for a company.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "ticker": {
                            "type": "string",
                            "description": "Stock ticker symbol"
                        },
                        "filing_type": {
                            "type": "string",
                            "description": "Filing type filter (10-K, 10-Q, 8-K, etc.)"
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of filings (default: 10)"
                        }
                    },
                    "required": ["ticker"]
                }
            },
            "get_news": {
                "description": "Fetch recent news for a stock from Yahoo Finance.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "ticker": {
                            "type": "string",
                            "description": "Stock ticker symbol"
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of news items (default: 10)"
                        },
                        "include_calendar": {
                            "type": "boolean",
                            "description": "Include upcoming events (earnings, dividends)"
                        }
                    },
                    "required": ["ticker"]
                }
            },
            "get_analyst_ratings": {
                "description": "Get analyst ratings, price targets, and recommendations for a stock.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "ticker": {
                            "type": "string",
                            "description": "Stock ticker symbol"
                        },
                        "include_earnings": {
                            "type": "boolean",
                            "description": "Include earnings estimates and history"
                        }
                    },
                    "required": ["ticker"]
                }
            }
        }

    async def handle_request(self, request: dict) -> dict:
        """Handle an MCP request."""
        method = request.get("method", "")
        params = request.get("params", {})
        request_id = request.get("id")

        if method == "initialize":
            return self._response(request_id, {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {}
                },
                "serverInfo": {
                    "name": "stock-research",
                    "version": "1.0.0"
                }
            })

        elif method == "tools/list":
            tools_list = []
            for name, spec in self.tools.items():
                tools_list.append({
                    "name": name,
                    "description": spec["description"],
                    "inputSchema": spec["inputSchema"]
                })
            return self._response(request_id, {"tools": tools_list})

        elif method == "tools/call":
            tool_name = params.get("name")
            arguments = params.get("arguments", {})
            result = await self._call_tool(tool_name, arguments)
            return self._response(request_id, {
                "content": [{"type": "text", "text": result}]
            })

        elif method == "notifications/initialized":
            # No response needed for notifications
            return None

        else:
            return self._error(request_id, -32601, f"Method not found: {method}")

    async def _call_tool(self, name: str, args: dict) -> str:
        """Execute a tool and return the result."""
        try:
            if name == "fetch_stock_data":
                return await self._fetch_stock_data(args)
            elif name == "run_dcf":
                return await self._run_dcf(args)
            elif name == "compare_stocks":
                return await self._compare_stocks(args)
            elif name == "get_sec_filings":
                return await self._get_sec_filings(args)
            elif name == "get_news":
                return await self._get_news(args)
            elif name == "get_analyst_ratings":
                return await self._get_analyst_ratings(args)
            else:
                return f"Unknown tool: {name}"
        except Exception as e:
            return f"Error executing {name}: {str(e)}"

    async def _fetch_stock_data(self, args: dict) -> str:
        """Fetch stock data."""
        from fetch_stock_data import fetch_stock_data, to_markdown
        ticker = args.get("ticker", "").upper()
        data = fetch_stock_data(ticker)
        return to_markdown(data)

    async def _run_dcf(self, args: dict) -> str:
        """Run DCF model."""
        from dcf_model import fetch_inputs_from_ticker, calculate_dcf, format_result
        import yfinance as yf

        ticker = args.get("ticker", "").upper()
        wacc = args.get("wacc", 0.09)
        terminal = args.get("terminal_growth", 0.025)

        inputs = fetch_inputs_from_ticker(ticker, wacc=wacc, terminal_growth=terminal)
        result = calculate_dcf(inputs)

        stock = yf.Ticker(ticker)
        current_price = stock.info.get('currentPrice') or stock.info.get('regularMarketPrice')

        return format_result(result, current_price)

    async def _compare_stocks(self, args: dict) -> str:
        """Compare stocks."""
        from compare_stocks import generate_comparison
        tickers = args.get("tickers", [])
        if len(tickers) < 2:
            return "Error: Need at least 2 tickers to compare"
        return generate_comparison(tickers)

    async def _get_sec_filings(self, args: dict) -> str:
        """Get SEC filings."""
        from sec_edgar import get_cik_from_ticker, get_company_filings, format_filings_markdown

        ticker = args.get("ticker", "").upper()
        filing_type = args.get("filing_type")
        limit = args.get("limit", 10)

        cik = get_cik_from_ticker(ticker)
        if not cik:
            return f"Error: Could not find CIK for {ticker}"

        filings = get_company_filings(cik, filing_type, limit)
        return format_filings_markdown(ticker, filings)

    async def _get_news(self, args: dict) -> str:
        """Get news."""
        from yahoo_news import get_stock_news, get_stock_calendar, format_news_markdown

        ticker = args.get("ticker", "").upper()
        limit = args.get("limit", 10)
        include_calendar = args.get("include_calendar", False)

        news = get_stock_news(ticker, limit)
        calendar = get_stock_calendar(ticker) if include_calendar else None

        return format_news_markdown(ticker, news, calendar)

    async def _get_analyst_ratings(self, args: dict) -> str:
        """Get analyst ratings."""
        from analyst_ratings import get_analyst_recommendations, get_earnings_estimates, format_ratings_markdown

        ticker = args.get("ticker", "").upper()
        include_earnings = args.get("include_earnings", False)

        data = get_analyst_recommendations(ticker)
        earnings = get_earnings_estimates(ticker) if include_earnings else None

        return format_ratings_markdown(data, earnings)

    def _response(self, request_id: Any, result: dict) -> dict:
        """Create a success response."""
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": result
        }

    def _error(self, request_id: Any, code: int, message: str) -> dict:
        """Create an error response."""
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "error": {"code": code, "message": message}
        }


async def main():
    """Main entry point - runs the MCP server over stdio."""
    server = MCPServer()

    # Read from stdin, write to stdout
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    await asyncio.get_event_loop().connect_read_pipe(lambda: protocol, sys.stdin)

    writer_transport, writer_protocol = await asyncio.get_event_loop().connect_write_pipe(
        asyncio.streams.FlowControlMixin, sys.stdout
    )
    writer = asyncio.StreamWriter(writer_transport, writer_protocol, reader, asyncio.get_event_loop())

    while True:
        try:
            # Read a line (JSON-RPC message)
            line = await reader.readline()
            if not line:
                break

            line = line.decode('utf-8').strip()
            if not line:
                continue

            # Parse request
            request = json.loads(line)

            # Handle request
            response = await server.handle_request(request)

            # Send response (if not a notification)
            if response is not None:
                response_json = json.dumps(response) + "\n"
                writer.write(response_json.encode('utf-8'))
                await writer.drain()

        except json.JSONDecodeError as e:
            error = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": f"Parse error: {e}"}
            }
            writer.write((json.dumps(error) + "\n").encode('utf-8'))
            await writer.drain()
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            break


if __name__ == "__main__":
    asyncio.run(main())
