"""
Example 5: Privacy Preservation

Demonstrates how sensitive data can be processed without entering the model's context.

Key benefit: PII and other sensitive information stays in the execution environment,
never being exposed to the model. This is crucial for compliance and security.
"""

import asyncio
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from servers import google_drive, salesforce
from client import get_mock_updates, clear_mock_updates


async def sync_customer_data():
    """
    Sync customer data between Google Sheets and Salesforce.

    The sensitive PII (emails, phone numbers, names) never enters
    the model's context—it flows directly between the tools.

    This is critical for:
    - GDPR compliance
    - HIPAA compliance
    - SOC 2 compliance
    - General data privacy best practices
    """
    print("Example 5: Privacy Preservation")
    print("=" * 60)
    print()

    clear_mock_updates()

    # Fetch customer data from Google Sheets
    print("Fetching customer data from Google Sheets...")
    result = await google_drive.get_sheet({'sheet_id': 'abc123'})
    sheet_rows = result['rows']

    print(f"Retrieved {len(sheet_rows)} customer records")
    print()

    # Process each row - PII stays in execution environment
    print("Syncing to Salesforce (PII remains in execution environment)...")

    for i, row in enumerate(sheet_rows, 1):
        # In a real implementation, this would use actual field mapping
        # For demo, we'll just track the updates
        await salesforce.update_record({
            'object_type': 'Lead',
            'record_id': f'L{i:03d}',
            'data': {
                'Email': row.get('email', 'N/A'),      # PII - never in model context
                'Phone': row.get('phone', 'N/A'),      # PII - never in model context
                'Name': row.get('name', 'N/A'),        # PII - never in model context
            }
        })

    print(f"✓ Updated {len(sheet_rows)} leads in Salesforce")
    print()

    # Show what happened (without exposing actual PII to model)
    updates = get_mock_updates()
    print("Summary of updates (no PII exposed):")
    print(f"  - Updated {len(updates)} customer records")
    print(f"  - Fields updated: Email, Phone, Name")
    print(f"  - All PII remained in execution environment")

    print()
    print("Key insight: Sensitive customer data never entered the model's context.")
    print("This approach enables:")
    print("  - GDPR/HIPAA/SOC2 compliance")
    print("  - Reduced data exposure risk")
    print("  - Audit trail without logging sensitive data")
    print("  - Automatic PII tokenization possibilities")


if __name__ == '__main__':
    asyncio.run(sync_customer_data())
