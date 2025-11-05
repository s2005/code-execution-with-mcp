# Errors and Fixes

This document details the errors discovered during example execution and the fixes applied.

## Date
2025-11-05

---

## Error 1: Missing f-string prefix in Example 02

### Location
`examples/02_data_filtering.py:69`

### Issue
The print statement was missing the `f` prefix for the f-string, causing the variable interpolation to fail.

### Original Code
```python
print("Key insight: All {len(all_rows)} rows were processed locally.")
```

### Error Observed
The output showed the literal string `{len(all_rows)}` instead of the actual number:
```
Key insight: All {len(all_rows)} rows were processed locally.
```

### Fix Applied
Added the `f` prefix to enable f-string formatting:
```python
print(f"Key insight: All {len(all_rows)} rows were processed locally.")
```

### Result After Fix
```
Key insight: All 5 rows were processed locally.
```

### Severity
Low - Cosmetic issue that did not affect functionality, only output formatting

---

## Error 2: Case-sensitivity in string matching in Example 03

### Location
`examples/03_control_flow.py:59`

### Issue
The code was checking for lowercase 'deployment complete' but the mock data contained 'Deployment complete' with a capital 'D', causing the message to never be found.

### Original Code
```python
found = any('deployment complete' in msg['text'] for msg in messages)
```

### Error Observed
The deployment notification was never detected:
```
Checking channel (attempt 1)...
  No deployment notification yet, waiting...
```

### Root Cause
The mock data in `client.py:65` has the message text as `'Deployment complete'` (capital D), but the check was case-sensitive and looking for lowercase.

### Fix Applied
Made the search case-insensitive by converting the message text to lowercase:
```python
found = any('deployment complete' in msg['text'].lower() for msg in messages)
```

### Result After Fix
```
Checking channel (attempt 1)...
✓ Deployment notification received!

Recent messages:
  - Starting deployment...
  - Running tests...
  - Tests passed!
  - Deployment complete
```

### Severity
Medium - Functional issue that prevented the example from demonstrating its intended behavior

---

## Summary

- **Total Examples**: 6
- **Examples with Issues**: 2
- **Examples Fixed**: 2
- **Final Status**: All examples passing ✅

All issues have been resolved and examples now run successfully without errors.
