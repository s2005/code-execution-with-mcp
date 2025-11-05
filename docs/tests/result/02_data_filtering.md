# Example 02: Data Filtering

## Description
Demonstrates how to filter and transform data in the execution environment before returning results to the model.

## Key Benefits
- Instead of loading thousands of rows into context, the agent processes them locally
- Only relevant summaries are presented to the model
- Dramatically reduces token usage for large datasets

## Execution Output

```
Example 2: Data Filtering
============================================================

Fetching order data from Google Sheets...
Retrieved 5 total orders

Found 3 pending orders

Pending orders (showing first 5):
  1. Order 1001: $150.0 - Acme Corp
  2. Order 1003: $175.5 - StartupXYZ
  3. Order 1004: $300.0 - BigCorp

Total pending order value: $625.50

Key insight: All 5 rows were processed locally.
Only 3 filtered results were shown to the model.
This dramatically reduces token usage for large datasets.
```

## Status
✅ Passed - Example executed successfully after fix

## Notes
- Initial execution had an f-string formatting issue (see errors_and_fixes.md)
- Issue was fixed and example now runs correctly

## Date
2025-11-05
