"""
Example 1: Cross-Tool Integration

Demonstrates how to integrate multiple MCP servers seamlessly.
This example reads a transcript from Google Drive and saves it to Salesforce.

Key benefit: The large transcript never passes through the model's context window—
it flows directly from Google Drive to Salesforce within the execution environment.
"""

import asyncio
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from servers import google_drive, salesforce
from client import get_mock_updates, clear_mock_updates


async def process_meeting_transcript():
    """
    Read a meeting transcript from Google Docs and add it to a Salesforce record.

    Without code execution:
    - Step 1: Call google_drive.get_document() -> 25,000 tokens in context
    - Step 2: Model processes transcript
    - Step 3: Call salesforce.update_record() -> Another 25,000 tokens
    - Total: ~50,000 extra tokens

    With code execution:
    - Agent writes code that calls both tools
    - Transcript flows directly between tools
    - Only summary goes to model
    - Total: Minimal token usage
    """
    print("Example 1: Cross-Tool Integration")
    print("=" * 60)
    print()

    # Clear any previous updates
    clear_mock_updates()

    # Fetch the transcript from Google Drive
    print("Fetching meeting transcript from Google Drive...")
    result = await google_drive.get_document({'document_id': 'abc123'})
    transcript = result['content']

    # Show a snippet of the transcript
    print(f"Retrieved transcript: {len(transcript)} characters")
    print(f"Preview: {transcript[:200]}...")
    print()

    # Update Salesforce record with the transcript
    print("Updating Salesforce record...")
    update_result = await salesforce.update_record({
        'object_type': 'SalesMeeting',
        'record_id': '00Q5f000001abcXYZ',
        'data': {'Notes': transcript}
    })

    print(f"Update successful: {update_result['success']}")
    print(f"Record ID: {update_result['record_id']}")
    print()

    # Show what was recorded
    updates = get_mock_updates()
    print("Recorded updates:")
    for update in updates:
        print(f"  - Updated {update['object_type']} record {update['record_id']}")
        print(f"    Field 'Notes' set to {len(update['data']['Notes'])} characters")

    print()
    print("Key insight: The transcript data never entered the model's context!")
    print("This approach saves ~50,000 tokens compared to calling tools directly.")


if __name__ == '__main__':
    asyncio.run(process_meeting_transcript())
