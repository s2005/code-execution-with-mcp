"""
Example 4: State Persistence

Demonstrates how to save intermediate results and pick up where you left off.

Key benefit: Agents can save progress and resume work across multiple executions,
enabling long-running workflows and better resource utilization.
"""

import asyncio
import csv
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from servers import salesforce


async def export_leads():
    """
    Export leads from Salesforce to a CSV file.

    This demonstrates persisting data to disk so it can be:
    - Processed later
    - Shared with other tools
    - Used across multiple agent executions
    """
    print("Example 4: State Persistence")
    print("=" * 60)
    print()

    # Ensure workspace directory exists
    os.makedirs('./workspace', exist_ok=True)

    # Query leads from Salesforce
    print("Querying leads from Salesforce...")
    result = await salesforce.query({
        'query': 'SELECT Id, Email, Name FROM Lead LIMIT 1000'
    })
    leads = result['records']

    print(f"Retrieved {len(leads)} leads")
    print()

    # Save to CSV
    csv_path = './workspace/leads.csv'
    print(f"Saving to {csv_path}...")

    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Id', 'Email', 'Name'])
        writer.writeheader()
        for lead in leads:
            writer.writerow(lead)

    print(f"✓ Saved {len(leads)} leads to CSV")
    print()

    # Demonstrate reading it back
    print("Reading back from saved file...")
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        saved_leads = list(reader)

    print(f"✓ Successfully loaded {len(saved_leads)} leads from disk")
    print()

    # Show sample data
    print("Sample leads:")
    for lead in saved_leads[:3]:
        print(f"  - {lead['Name']} ({lead['Email']})")

    print()
    print("Key insight: The data is now persisted on disk.")
    print("A future execution can pick up from here without re-querying Salesforce.")
    print("This enables long-running workflows and better resource management.")


if __name__ == '__main__':
    asyncio.run(export_leads())
