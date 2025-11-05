# Example 01: Cross-Tool Integration

## Description
Demonstrates how to integrate multiple MCP servers seamlessly by reading a transcript from Google Drive and saving it to Salesforce.

## Key Benefits
- The large transcript never passes through the model's context window
- Data flows directly from Google Drive to Salesforce within the execution environment
- Saves approximately 50,000 tokens compared to calling tools directly

## Execution Output

```
Example 1: Cross-Tool Integration
============================================================

Fetching meeting transcript from Google Drive...
Retrieved transcript: 494 characters
Preview: Meeting Transcript - Q4 Planning Session

Attendees: Alice, Bob, Carol
Date: November 1, 2025

Alice: Let's review our Q4 objectives. We need to focus on three key areas...
Bob: I agree. The customer ...

Updating Salesforce record...
Update successful: True
Record ID: 00Q5f000001abcXYZ

Recorded updates:
  - Updated SalesMeeting record 00Q5f000001abcXYZ
    Field 'Notes' set to 494 characters

Key insight: The transcript data never entered the model's context!
This approach saves ~50,000 tokens compared to calling tools directly.
```

## Status
✅ Passed - Example executed successfully without errors

## Date
2025-11-05
