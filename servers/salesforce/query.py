"""Query Salesforce records"""

from typing import TypedDict, List, Dict, Any
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from client import call_mcp_tool


class QueryInput(TypedDict):
    """Input parameters for querying Salesforce"""
    query: str


class QueryResponse(TypedDict):
    """Response from querying Salesforce"""
    records: List[Dict[str, Any]]


async def query(input: QueryInput) -> QueryResponse:
    """
    Query records from Salesforce.

    Args:
        input: Dictionary containing SOQL query string

    Returns:
        Dictionary containing list of matching records
    """
    result = await call_mcp_tool('salesforce__query', input)
    return result  # type: ignore
