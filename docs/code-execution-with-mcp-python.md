# Code Execution with MCP: Building More Efficient AI Agents (Python Edition)

*Based on the original article by Adam Jones and Conor Kelly at Anthropic*

## Overview

This article explores how code execution environments can improve AI agent efficiency when integrated with the Model Context Protocol (MCP), demonstrated through Python examples.

## The Core Problem

When agents connect to numerous MCP servers, two inefficiencies emerge:

### 1. Tool Definition Overhead

Tool descriptions occupy more context window space, increasing response time and costs. When connecting to multiple MCP servers with dozens of tools each, the context window fills up quickly with tool definitions alone.

### 2. Intermediate Result Bloat

Each tool result passes through the model's context. Consider this scenario:

**Without Code Execution:**
1. Agent calls `google_drive.get_document('meeting-transcript')` → Returns 25,000 token transcript
2. Agent analyzes transcript in context
3. Agent calls `salesforce.update_record(...)` → Passes transcript again
4. Result: ~50,000 extra tokens consumed for the intermediate data

**With Code Execution:**
1. Agent writes code that calls both tools internally
2. Only the final summary passes through the model
3. Result: Minimal token usage

## The Solution: Treat MCP Servers as Code APIs

Rather than exposing tools as direct function calls to the model, agents treat MCP servers as importable Python modules. The implementation uses a filesystem structure where each tool becomes a callable Python function.

### Example Architecture

```
servers/
├── google_drive/
│   ├── __init__.py
│   ├── get_document.py
│   └── get_sheet.py
├── salesforce/
│   ├── __init__.py
│   ├── update_record.py
│   └── query.py
└── slack/
    ├── __init__.py
    └── get_channel_history.py
```

Agents discover tools on-demand by exploring directories, loading only necessary definitions. This approach can reduce token usage from 150,000 to 2,000 tokens—a **98.7% reduction**.

## Implementation Examples

### 1. Basic Tool Wrapper (Google Drive)

```python
# ./servers/google_drive/get_document.py
from typing import TypedDict
from client import call_mcp_tool

class GetDocumentInput(TypedDict):
    document_id: str

class GetDocumentResponse(TypedDict):
    content: str

async def get_document(input: GetDocumentInput) -> GetDocumentResponse:
    """Read a document from Google Drive"""
    return await call_mcp_tool('google_drive__get_document', input)
```

### 2. Cross-Tool Integration

One of the most powerful benefits is seamless integration across multiple MCP servers:

```python
# Read transcript from Google Docs and add to Salesforce prospect
from servers import google_drive, salesforce

async def process_meeting_transcript():
    # Fetch the transcript
    result = await google_drive.get_document({'document_id': 'abc123'})
    transcript = result['content']

    # Update Salesforce record
    await salesforce.update_record({
        'object_type': 'SalesMeeting',
        'record_id': '00Q5f000001abcXYZ',
        'data': {'Notes': transcript}
    })
```

**Key Advantage:** The massive transcript never passes through the model's context window—it flows directly from Google Drive to Salesforce within the execution environment.

### 3. Data Filtering

Agents can filter and transform results in code before returning them to the model:

```python
# With code execution - filter in the execution environment
all_rows = await google_drive.get_sheet({'sheet_id': 'abc123'})
pending_orders = [
    row for row in all_rows
    if row.get("Status") == 'pending'
]

print(f"Found {len(pending_orders)} pending orders")
print(pending_orders[:5])  # Only show first 5 for review
```

Instead of loading thousands of rows into context, the agent processes them in the execution environment and only presents relevant summaries.

### 4. Control Flow with Loops

Native Python control flow eliminates the need for complex multi-step tool orchestration:

```python
import asyncio

async def wait_for_deployment():
    found = False
    while not found:
        messages = await slack.get_channel_history({'channel': 'C123456'})
        found = any('deployment complete' in m['text'] for m in messages)
        if not found:
            await asyncio.sleep(5)

    print('Deployment notification received')
```

Without code execution, this would require multiple rounds of model inference and tool calls.

### 5. State Persistence

Agents can save intermediate results and pick up where they left off:

```python
import aiofiles
import csv

# Initial execution
async def export_leads():
    leads = await salesforce.query({
        'query': 'SELECT Id, Email FROM Lead LIMIT 1000'
    })

    async with aiofiles.open('./workspace/leads.csv', 'w') as f:
        writer = csv.writer(f)
        await writer.writerow(['Id', 'Email'])
        for lead in leads:
            await writer.writerow([lead['Id'], lead['Email']])

# Later execution picks up where it left off
async def process_saved_leads():
    async with aiofiles.open('./workspace/leads.csv', 'r') as f:
        reader = csv.DictReader(f)
        leads = [row async for row in reader]
    # Continue processing...
```

### 6. Reusable Skills

Agents can save commonly used operations as reusable functions:

```python
# In ./skills/save_sheet_as_csv.py
from servers import google_drive
import aiofiles
import csv

async def save_sheet_as_csv(sheet_id: str) -> str:
    """Download a Google Sheet and save as CSV"""
    data = await google_drive.get_sheet({'sheet_id': sheet_id})

    file_path = f'./workspace/sheet-{sheet_id}.csv'
    async with aiofiles.open(file_path, 'w') as f:
        writer = csv.writer(f)
        for row in data:
            await writer.writerow(row)

    return file_path

# Later, in any agent execution:
from skills.save_sheet_as_csv import save_sheet_as_csv

csv_path = await save_sheet_as_csv('abc123')
```

### 7. Privacy Preservation

Sensitive data can be processed without entering the model's context:

```python
async def sync_customer_data():
    """Sync customer data while keeping PII out of model context"""
    sheet = await google_drive.get_sheet({'sheet_id': 'abc123'})

    for row in sheet:
        await salesforce.update_record({
            'object_type': 'Lead',
            'record_id': row['salesforce_id'],
            'data': {
                'Email': row['email'],      # PII stays in execution env
                'Phone': row['phone'],      # Never enters model context
                'Name': row['name']
            }
        })

    # Only the summary goes to the model
    print(f"Updated {len(sheet)} leads")
```

The agent can even implement automatic PII tokenization before any data reaches the model.

## Key Benefits

### Progressive Disclosure
Models navigate the filesystem to access tools incrementally, loading only what they need.

### Data Filtering
Agents filter and transform results in code before returning them to the model, drastically reducing token usage.

### Privacy Preservation
Intermediate data stays in execution environments. Sensitive fields can be tokenized automatically before reaching the model.

### State Persistence
Agents save intermediate results and reusable code as "skills" that can be invoked in future executions.

### Better Control Flow
Native loops, conditionals, and error handling replace chained tool calls and complex multi-step orchestration.

### Cost Reduction
Token usage drops by up to 98.7% by keeping intermediate data out of the context window.

## Important Tradeoff

This approach requires secure code execution environments with:

- **Sandboxing**: Isolated execution to prevent unauthorized access
- **Resource Limits**: CPU, memory, and time constraints
- **Network Controls**: Restricted outbound connections
- **Monitoring**: Logging and auditing of code execution

This adds infrastructure complexity that direct tool calls avoid. However, for production AI agents handling sensitive data or complex workflows, these security measures are often necessary anyway.

## Implementation Considerations

### Python-Specific Advantages

1. **Rich Ecosystem**: Leverage existing Python libraries for data processing (pandas, numpy)
2. **Async/Await**: Native support for concurrent operations
3. **Type Hints**: Clear interfaces with `TypedDict` and `dataclasses`
4. **Error Handling**: Standard try/except patterns
5. **Testing**: Familiar pytest ecosystem for validation

### Example with Data Processing

```python
import pandas as pd
from servers import google_drive, salesforce

async def analyze_sales_data():
    # Fetch raw data
    sheet_data = await google_drive.get_sheet({'sheet_id': 'sales-2024'})

    # Process with pandas (in execution environment)
    df = pd.DataFrame(sheet_data)
    summary = df.groupby('Region')['Sales'].agg(['sum', 'mean', 'count'])

    # Only return the summary to the model
    return summary.to_dict()
```

## Getting Started

1. Set up your MCP servers
2. Create the `servers/` directory structure
3. Implement tool wrappers for each MCP tool
4. Configure a secure code execution environment
5. Enable your agent to discover and call tools via code

## Conclusion

By treating MCP servers as code APIs rather than direct tool calls, agents gain:

- **Efficiency**: 98.7% reduction in token usage
- **Privacy**: Sensitive data never enters model context
- **Flexibility**: Full programming language capabilities
- **Maintainability**: Reusable skills and clear abstractions

While this approach requires more infrastructure, the benefits for production AI agents are substantial. The combination of Python's ecosystem and MCP's standardization creates a powerful foundation for building efficient, secure, and capable AI agents.

---

*Original article: [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)*
*Authors: Adam Jones and Conor Kelly, Anthropic*
