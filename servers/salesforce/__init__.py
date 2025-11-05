"""Salesforce MCP Server Tools"""

from .update_record import update_record, UpdateRecordInput, UpdateRecordResponse
from .query import query, QueryInput, QueryResponse

__all__ = [
    'update_record',
    'UpdateRecordInput',
    'UpdateRecordResponse',
    'query',
    'QueryInput',
    'QueryResponse',
]
