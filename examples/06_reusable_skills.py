"""
Example 6: Reusable Skills

Demonstrates how agents can save commonly used operations as reusable functions.

Key benefit: Build a library of tested, reusable skills that can be composed
into more complex workflows. This improves reliability and reduces development time.
"""

import asyncio
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from skills import save_sheet_as_csv


async def use_reusable_skill():
    """
    Use a pre-built skill to save a Google Sheet as CSV.

    Skills are functions that encapsulate common operations.
    They can be:
    - Tested independently
    - Reused across multiple workflows
    - Composed together for complex tasks
    - Maintained and versioned separately
    """
    print("Example 6: Reusable Skills")
    print("=" * 60)
    print()

    # Use the skill to save a sheet as CSV
    print("Using reusable skill: save_sheet_as_csv")
    print()

    sheet_id = 'abc123'
    print(f"Converting Google Sheet '{sheet_id}' to CSV...")

    # Call the skill
    csv_path = await save_sheet_as_csv(sheet_id)

    print(f"✓ Sheet saved to: {csv_path}")
    print()

    # Verify the file exists and show its contents
    if os.path.exists(csv_path):
        file_size = os.path.getsize(csv_path)
        print(f"File size: {file_size} bytes")
        print()

        # Show first few lines
        print("File preview:")
        with open(csv_path, 'r') as f:
            for i, line in enumerate(f):
                if i >= 4:  # Show first 4 lines
                    break
                print(f"  {line.rstrip()}")

    print()
    print("Key insight: Reusable skills enable:")
    print("  - Code reuse across multiple workflows")
    print("  - Independent testing and validation")
    print("  - Faster development of complex agents")
    print("  - Better maintainability")
    print()
    print("Agents can build up a library of skills over time,")
    print("making them more capable with each new skill learned.")


if __name__ == '__main__':
    asyncio.run(use_reusable_skill())
