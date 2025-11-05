"""
MCP Client for calling tools on MCP servers.

This module provides a simple interface for calling MCP tools from Python code.
In a real implementation, this would connect to actual MCP servers.
For demonstration purposes, this includes mock implementations.
"""

import asyncio
from typing import Any, Dict, TypeVar, cast

T = TypeVar('T')

# Mock data for demonstration
MOCK_DATA = {
    'google_drive__get_document': {
        'abc123': {
            'content': '''Meeting Transcript - Q4 Planning Session

Attendees: Alice, Bob, Carol
Date: November 1, 2025

Alice: Let's review our Q4 objectives. We need to focus on three key areas...
Bob: I agree. The customer feedback has been clear about what they want...
Carol: We should also consider the resource allocation for these initiatives...

[... 24,000 more tokens of transcript ...]

Action Items:
1. Alice to prepare budget proposal
2. Bob to gather customer requirements
3. Carol to draft resource plan
'''
        }
    },
    'google_drive__get_sheet': {
        'abc123': [
            {'Order ID': '1001', 'Status': 'pending', 'Amount': 150.00, 'Customer': 'Acme Corp'},
            {'Order ID': '1002', 'Status': 'completed', 'Amount': 200.00, 'Customer': 'TechCo'},
            {'Order ID': '1003', 'Status': 'pending', 'Amount': 175.50, 'Customer': 'StartupXYZ'},
            {'Order ID': '1004', 'Status': 'pending', 'Amount': 300.00, 'Customer': 'BigCorp'},
            {'Order ID': '1005', 'Status': 'shipped', 'Amount': 125.00, 'Customer': 'SmallBiz'},
        ],
        'sales-2024': [
            {'Region': 'North', 'Sales': 45000, 'Quarter': 'Q1'},
            {'Region': 'South', 'Sales': 38000, 'Quarter': 'Q1'},
            {'Region': 'North', 'Sales': 52000, 'Quarter': 'Q2'},
            {'Region': 'South', 'Sales': 41000, 'Quarter': 'Q2'},
            {'Region': 'North', 'Sales': 48000, 'Quarter': 'Q3'},
            {'Region': 'South', 'Sales': 44000, 'Quarter': 'Q3'},
        ]
    },
    'salesforce__query': {
        'leads': [
            {'Id': 'L001', 'Email': 'contact1@example.com', 'Name': 'John Doe'},
            {'Id': 'L002', 'Email': 'contact2@example.com', 'Name': 'Jane Smith'},
            {'Id': 'L003', 'Email': 'contact3@example.com', 'Name': 'Bob Johnson'},
        ]
    },
    'slack__get_channel_history': {
        'C123456': [
            {'text': 'Starting deployment...', 'timestamp': '1699000000'},
            {'text': 'Running tests...', 'timestamp': '1699000060'},
            {'text': 'Tests passed!', 'timestamp': '1699000120'},
            {'text': 'Deployment complete', 'timestamp': '1699000180'},
        ]
    }
}

# Track updates for demonstration
MOCK_UPDATES: list[Dict[str, Any]] = []


async def call_mcp_tool(tool_name: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
    """
    Call an MCP tool and return the result.

    In a real implementation, this would:
    1. Connect to the appropriate MCP server
    2. Send the tool call request
    3. Wait for and return the response

    For demonstration, this returns mock data.

    Args:
        tool_name: The name of the MCP tool to call
        parameters: The parameters to pass to the tool

    Returns:
        The tool's response as a dictionary
    """
    # Simulate network latency
    await asyncio.sleep(0.1)

    # Handle different tool calls
    if tool_name == 'google_drive__get_document':
        doc_id = parameters.get('document_id', parameters.get('documentId'))
        data = MOCK_DATA['google_drive__get_document'].get(doc_id, {'content': 'Document not found'})
        return cast(Dict[str, Any], data)

    elif tool_name == 'google_drive__get_sheet':
        sheet_id = parameters.get('sheet_id', parameters.get('sheetId'))
        data = MOCK_DATA['google_drive__get_sheet'].get(sheet_id, [])
        return cast(Dict[str, Any], {'rows': data})

    elif tool_name == 'salesforce__update_record':
        # Record the update for demonstration
        update_record = {
            'tool': 'salesforce__update_record',
            'object_type': parameters.get('object_type', parameters.get('objectType')),
            'record_id': parameters.get('record_id', parameters.get('recordId')),
            'data': parameters.get('data')
        }
        MOCK_UPDATES.append(update_record)
        return {'success': True, 'record_id': parameters.get('record_id', parameters.get('recordId'))}

    elif tool_name == 'salesforce__query':
        query = parameters.get('query', '')
        if 'Lead' in query:
            return {'records': MOCK_DATA['salesforce__query']['leads']}
        return {'records': []}

    elif tool_name == 'slack__get_channel_history':
        channel = parameters.get('channel')
        messages = MOCK_DATA['slack__get_channel_history'].get(channel, [])
        return {'messages': messages}

    else:
        raise ValueError(f"Unknown tool: {tool_name}")


def get_mock_updates() -> list[Dict[str, Any]]:
    """Get all recorded mock updates for demonstration purposes."""
    return MOCK_UPDATES.copy()


def clear_mock_updates() -> None:
    """Clear all recorded mock updates."""
    MOCK_UPDATES.clear()
