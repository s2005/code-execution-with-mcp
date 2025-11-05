"""
Run all examples in sequence.

This script runs all the examples to demonstrate the key concepts
of code execution with MCP.
"""

import asyncio
import subprocess
import sys
import os


async def run_example(script_name: str, description: str):
    """Run a single example script."""
    print("\n" + "=" * 70)
    print(f"Running: {description}")
    print("=" * 70 + "\n")

    # Run the script
    result = subprocess.run(
        [sys.executable, script_name],
        cwd=os.path.dirname(os.path.abspath(__file__)),
        capture_output=False
    )

    if result.returncode != 0:
        print(f"\n❌ Example failed with return code {result.returncode}")
        return False

    print("\n✓ Example completed successfully")
    return True


async def main():
    """Run all examples."""
    print("=" * 70)
    print("Code Execution with MCP - Python Examples")
    print("=" * 70)
    print()
    print("This demonstrates the key concepts from Anthropic's article:")
    print("https://www.anthropic.com/engineering/code-execution-with-mcp")
    print()

    examples = [
        ("examples/01_cross_tool_integration.py", "Cross-Tool Integration"),
        ("examples/02_data_filtering.py", "Data Filtering"),
        ("examples/03_control_flow.py", "Control Flow with Loops"),
        ("examples/04_state_persistence.py", "State Persistence"),
        ("examples/05_privacy_preservation.py", "Privacy Preservation"),
        ("examples/06_reusable_skills.py", "Reusable Skills"),
    ]

    results = []
    for script, description in examples:
        success = await run_example(script, description)
        results.append((description, success))
        await asyncio.sleep(0.5)  # Brief pause between examples

    # Summary
    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)

    for description, success in results:
        status = "✓" if success else "❌"
        print(f"{status} {description}")

    total = len(results)
    passed = sum(1 for _, success in results if success)

    print()
    print(f"Completed: {passed}/{total} examples")

    if passed == total:
        print("\n🎉 All examples ran successfully!")
        print()
        print("Key takeaway: Code execution with MCP enables:")
        print("  • 98.7% reduction in token usage")
        print("  • Privacy preservation for sensitive data")
        print("  • Better control flow and error handling")
        print("  • State persistence across executions")
        print("  • Reusable skills and abstractions")


if __name__ == '__main__':
    asyncio.run(main())
