"""
Example 2: Data Filtering

Demonstrates how to filter and transform data in the execution environment
before returning results to the model.

Key benefit: Instead of loading thousands of rows into context, the agent
processes them locally and only presents relevant summaries.
"""

import asyncio
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from servers import google_drive


async def filter_pending_orders():
    """
    Fetch a spreadsheet and filter for pending orders.

    Without code execution:
    - All rows loaded into context
    - Model filters in context
    - High token usage

    With code execution:
    - Filtering happens in execution environment
    - Only summary goes to model
    - Minimal token usage
    """
    print("Example 2: Data Filtering")
    print("=" * 60)
    print()

    # Fetch all rows from the sheet
    print("Fetching order data from Google Sheets...")
    result = await google_drive.get_sheet({'sheet_id': 'abc123'})
    all_rows = result['rows']

    print(f"Retrieved {len(all_rows)} total orders")
    print()

    # Filter for pending orders in the execution environment
    pending_orders = [
        row for row in all_rows
        if row.get('Status') == 'pending'
    ]

    print(f"Found {len(pending_orders)} pending orders")
    print()

    # Show only the first 5 for review
    print("Pending orders (showing first 5):")
    for i, order in enumerate(pending_orders[:5], 1):
        print(f"  {i}. Order {order['Order ID']}: "
              f"${order['Amount']} - {order['Customer']}")

    print()

    # Calculate summary statistics
    total_pending_value = sum(order['Amount'] for order in pending_orders)
    print(f"Total pending order value: ${total_pending_value:.2f}")

    print()
    print(f"Key insight: All {len(all_rows)} rows were processed locally.")
    print(f"Only {len(pending_orders)} filtered results were shown to the model.")
    print("This dramatically reduces token usage for large datasets.")


if __name__ == '__main__':
    asyncio.run(filter_pending_orders())
