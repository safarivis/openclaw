#!/usr/bin/env python3
"""
Agent Structure Test Runner

Tests agent workspaces against knowledge base standards.
Run from clawd-lab directory: python knowledge/evals/run_tests.py

KISS: Only tests what we can verify without running the agent.
"""

import os
import re
import sys
import yaml
from pathlib import Path
from datetime import datetime


# Agent directories to test (relative to clawd-lab)
AGENT_DIRS = [
    "factory",
    "agent-reviewer",
    "info-agent",
    "brand-agent",
]

# Colors for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"


def load_test_config():
    """Load test configuration from YAML."""
    config_path = Path(__file__).parent / "tests" / "structure.yaml"
    with open(config_path) as f:
        return yaml.safe_load(f)


def check_file_exists(agent_path: Path, filename: str) -> tuple[bool, str]:
    """Check if a file or directory exists."""
    path = agent_path / filename
    exists = path.exists()
    status = "exists" if exists else "MISSING"
    return exists, status


def check_pattern_in_file(filepath: Path, pattern: str, min_occurrences: int = 1) -> tuple[bool, int]:
    """Check if a regex pattern appears in a file."""
    if not filepath.exists():
        return False, 0

    content = filepath.read_text()
    matches = re.findall(pattern, content, re.IGNORECASE)
    count = len(matches)
    return count >= min_occurrences, count


def test_agent(agent_dir: str, config: dict) -> dict:
    """Run all structure tests on an agent."""
    agent_path = Path(agent_dir)
    results = {
        "agent": agent_dir,
        "passed": 0,
        "failed": 0,
        "warnings": 0,
        "details": []
    }

    # Test required files
    for filename in config["required_files"]:
        passed, status = check_file_exists(agent_path, filename)
        results["details"].append({
            "test": f"Required: {filename}",
            "passed": passed,
            "status": status
        })
        if passed:
            results["passed"] += 1
        else:
            results["failed"] += 1

    # Test recommended files (warnings only)
    for filename in config["recommended_files"]:
        passed, status = check_file_exists(agent_path, filename)
        results["details"].append({
            "test": f"Recommended: {filename}",
            "passed": passed,
            "status": status,
            "warning": not passed
        })
        if passed:
            results["passed"] += 1
        else:
            results["warnings"] += 1

    # Test AGENTS.md patterns
    agents_file = agent_path / "AGENTS.md"
    for check in config["agents_md_checks"]:
        passed, count = check_pattern_in_file(
            agents_file,
            check["pattern"],
            check["min_occurrences"]
        )
        results["details"].append({
            "test": f"AGENTS.md: {check['description']}",
            "passed": passed,
            "status": f"found {count}x" if passed else f"only {count}x (need {check['min_occurrences']})"
        })
        if passed:
            results["passed"] += 1
        else:
            results["failed"] += 1

    # Test TOOLS.md patterns
    tools_file = agent_path / "TOOLS.md"
    for check in config["tools_md_checks"]:
        passed, count = check_pattern_in_file(
            tools_file,
            check["pattern"],
            check["min_occurrences"]
        )
        results["details"].append({
            "test": f"TOOLS.md: {check['description']}",
            "passed": passed,
            "status": f"found {count}x" if passed else f"only {count}x (need {check['min_occurrences']})"
        })
        if passed:
            results["passed"] += 1
        else:
            results["failed"] += 1

    # Test IDENTITY.md patterns
    identity_file = agent_path / "IDENTITY.md"
    for check in config["identity_md_checks"]:
        passed, count = check_pattern_in_file(
            identity_file,
            check["pattern"],
            check["min_occurrences"]
        )
        results["details"].append({
            "test": f"IDENTITY.md: {check['description']}",
            "passed": passed,
            "status": f"found {count}x" if passed else f"only {count}x"
        })
        if passed:
            results["passed"] += 1
        else:
            results["failed"] += 1

    # Test SOUL.md patterns
    soul_file = agent_path / "SOUL.md"
    for check in config["soul_md_checks"]:
        passed, count = check_pattern_in_file(
            soul_file,
            check["pattern"],
            check["min_occurrences"]
        )
        results["details"].append({
            "test": f"SOUL.md: {check['description']}",
            "passed": passed,
            "status": f"found {count}x" if passed else f"only {count}x"
        })
        if passed:
            results["passed"] += 1
        else:
            results["failed"] += 1

    return results


def print_results(all_results: list[dict], verbose: bool = False):
    """Print test results."""
    print(f"\n{BOLD}{'=' * 60}{RESET}")
    print(f"{BOLD}              AGENT STRUCTURE TEST RESULTS{RESET}")
    print(f"{BOLD}{'=' * 60}{RESET}\n")

    total_passed = 0
    total_failed = 0
    total_warnings = 0

    for result in all_results:
        agent = result["agent"]
        passed = result["passed"]
        failed = result["failed"]
        warnings = result["warnings"]
        total = passed + failed

        total_passed += passed
        total_failed += failed
        total_warnings += warnings

        # Calculate score
        score = (passed / total * 100) if total > 0 else 0

        # Status color
        if failed == 0:
            color = GREEN
            status = "PASS"
        elif failed <= 2:
            color = YELLOW
            status = "WARN"
        else:
            color = RED
            status = "FAIL"

        # Progress bar
        bar_width = 20
        filled = int(bar_width * passed / total) if total > 0 else 0
        bar = "█" * filled + "░" * (bar_width - filled)

        print(f"  {agent:20} {bar} {passed}/{total} ({score:.0f}%) {color}[{status}]{RESET}")

        # Verbose: show details
        if verbose:
            for detail in result["details"]:
                icon = f"{GREEN}✓{RESET}" if detail["passed"] else f"{RED}✗{RESET}"
                if detail.get("warning"):
                    icon = f"{YELLOW}⚠{RESET}"
                print(f"      {icon} {detail['test']}: {detail['status']}")
            print()

    # Summary
    total = total_passed + total_failed
    overall_score = (total_passed / total * 100) if total > 0 else 0

    print(f"\n{BOLD}{'─' * 60}{RESET}")
    print(f"  TOTAL: {total_passed}/{total} passed ({overall_score:.0f}%)")
    if total_warnings > 0:
        print(f"  {YELLOW}Warnings: {total_warnings} (recommended files missing){RESET}")
    if total_failed > 0:
        print(f"  {RED}Failed: {total_failed} checks need attention{RESET}")
    print(f"{BOLD}{'─' * 60}{RESET}\n")

    return total_failed == 0


def main():
    """Main entry point."""
    # Parse args
    verbose = "-v" in sys.argv or "--verbose" in sys.argv

    # Find project root (clawd-lab)
    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent.parent  # knowledge/evals -> knowledge -> clawd-lab
    os.chdir(project_root)

    print(f"\nRunning tests from: {project_root}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Load config
    config = load_test_config()

    # Run tests on all agents
    all_results = []
    for agent_dir in AGENT_DIRS:
        if Path(agent_dir).exists():
            results = test_agent(agent_dir, config)
            all_results.append(results)
        else:
            print(f"{YELLOW}Warning: {agent_dir} not found, skipping{RESET}")

    # Print results
    success = print_results(all_results, verbose)

    # Exit code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
