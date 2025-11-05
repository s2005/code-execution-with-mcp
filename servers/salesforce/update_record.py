"""Update a Salesforce record"""

from typing import TypedDict, Dict, Any
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from client import call_mcp_tool


class UpdateRecordInput(TypedDict):
    """Input parameters for updating a Salesforce record"""
    object_type: str
    record_id: str
    data: Dict[str, Any]


class UpdateRecordResponse(TypedDict):
    """Response from updating a Salesforce record"""
    success: bool
    record_id: str


async def update_record(input: UpdateRecordInput) -> UpdateRecordResponse:
    """
    Update a record in Salesforce.

    Args:
        input: Dictionary containing object_type, record_id, and data

    Returns:
        Dictionary containing success status and record_id
    """
    result = await call_mcp_tool('salesforce__update_record', input)
    return result  # type: ignore
