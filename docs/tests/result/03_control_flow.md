# Example 03: Control Flow with Loops

## Description
Demonstrates using native Python control flow (loops, conditionals) to handle complex workflows such as polling a Slack channel for deployment notifications.

## Key Benefits
- Eliminates the need for complex multi-step tool orchestration
- Single code block with loop instead of multiple model inference rounds
- Much faster and more efficient than calling tools repeatedly

## Execution Output

```
Example 3: Control Flow with Loops
============================================================

Waiting for deployment notification in Slack channel...

Checking channel (attempt 1)...
✓ Deployment notification received!

Recent messages:
  - Starting deployment...
  - Running tests...
  - Tests passed!
  - Deployment complete

Key insight: This entire polling loop runs in one execution.
Without code execution, each check would require a separate
model inference call, making it much slower and more expensive.
```

## Status
✅ Passed - Example executed successfully after fix

## Notes
- Initial execution had a case-sensitivity issue in message matching (see errors_and_fixes.md)
- Issue was fixed and example now correctly detects deployment completion

## Date
2025-11-05
