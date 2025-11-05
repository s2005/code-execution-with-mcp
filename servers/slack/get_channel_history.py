"""Get Slack channel message history"""

from typing import TypedDict, List, Dict, Any
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from client import call_mcp_tool


class GetChannelHistoryInput(TypedDict):
    """Input parameters for getting Slack channel history"""
    channel: str


class GetChannelHistoryResponse(TypedDict):
    """Response from getting Slack channel history"""
    messages: List[Dict[str, Any]]


async def get_channel_history(input: GetChannelHistoryInput) -> GetChannelHistoryResponse:
    """
    Get message history from a Slack channel.

    Args:
        input: Dictionary containing channel ID

    Returns:
        Dictionary containing list of messages
    """
    result = await call_mcp_tool('slack__get_channel_history', input)
    return result  # type: ignore
