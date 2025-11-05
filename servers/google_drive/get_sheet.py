"""Get a spreadsheet from Google Drive"""

from typing import TypedDict, List, Dict, Any
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from client import call_mcp_tool


class GetSheetInput(TypedDict):
    """Input parameters for getting a Google Sheet"""
    sheet_id: str


class GetSheetResponse(TypedDict):
    """Response from getting a Google Sheet"""
    rows: List[Dict[str, Any]]


async def get_sheet(input: GetSheetInput) -> GetSheetResponse:
    """
    Read a spreadsheet from Google Drive.

    Args:
        input: Dictionary containing sheet_id

    Returns:
        Dictionary containing rows of data
    """
    result = await call_mcp_tool('google_drive__get_sheet', input)
    return result  # type: ignore
