"""Get a document from Google Drive"""

from typing import TypedDict
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from client import call_mcp_tool


class GetDocumentInput(TypedDict):
    """Input parameters for getting a Google Drive document"""
    document_id: str


class GetDocumentResponse(TypedDict):
    """Response from getting a Google Drive document"""
    content: str


async def get_document(input: GetDocumentInput) -> GetDocumentResponse:
    """
    Read a document from Google Drive.

    Args:
        input: Dictionary containing document_id

    Returns:
        Dictionary containing the document content
    """
    result = await call_mcp_tool('google_drive__get_document', input)
    return result  # type: ignore
