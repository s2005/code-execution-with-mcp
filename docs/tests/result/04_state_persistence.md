# Example 04: State Persistence

## Description
Demonstrates how to save intermediate results to disk and pick up where you left off, enabling long-running workflows.

## Key Benefits
- Agents can save progress and resume work across multiple executions
- Data can be processed later, shared with other tools, or used across multiple agent executions
- Enables better resource utilization and management

## Execution Output

```
Example 4: State Persistence
============================================================

Querying leads from Salesforce...
Retrieved 3 leads

Saving to ./workspace/leads.csv...
✓ Saved 3 leads to CSV

Reading back from saved file...
✓ Successfully loaded 3 leads from disk

Sample leads:
  - John Doe (contact1@example.com)
  - Jane Smith (contact2@example.com)
  - Bob Johnson (contact3@example.com)

Key insight: The data is now persisted on disk.
A future execution can pick up from here without re-querying Salesforce.
This enables long-running workflows and better resource management.
```

## Status
✅ Passed - Example executed successfully without errors

## Date
2025-11-05
