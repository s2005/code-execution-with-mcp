# Code Execution with MCP - Python Examples

This repository contains Python implementations and examples based on Anthropic's article on code execution with the Model Context Protocol (MCP).

## Original Article

[Code Execution with MCP: Building More Efficient AI Agents](https://www.anthropic.com/engineering/code-execution-with-mcp)

Written by Adam Jones and Conor Kelly at Anthropic (Published: November 4, 2025)

## Overview

This project demonstrates how to build more efficient AI agents by treating MCP servers as code APIs rather than direct tool calls. The approach can reduce token usage by up to 98.7% while improving privacy, control flow, and maintainability.

## Contents

- **[docs/code-execution-with-mcp-python.md](docs/code-execution-with-mcp-python.md)** - Python version of the article with detailed explanations and code examples
- **examples/** - Working Python implementations demonstrating the concepts
- **servers/** - Example MCP server wrappers
- **skills/** - Reusable agent skills

## Key Benefits

- **98.7% reduction in token usage** by keeping intermediate data out of context
- **Privacy preservation** - sensitive data stays in execution environment
- **Better control flow** - use native Python loops and conditionals
- **State persistence** - save and reuse intermediate results
- **Reusable skills** - build a library of common operations

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run example: Cross-tool integration
python examples/01_cross_tool_integration.py

# Run example: Data filtering
python examples/02_data_filtering.py

# Run example: Control flow
python examples/03_control_flow.py
```

## Project Structure

```
.
├── README.md
├── docs/
│   └── code-execution-with-mcp-python.md
├── examples/
│   ├── 01_cross_tool_integration.py
│   ├── 02_data_filtering.py
│   ├── 03_control_flow.py
│   ├── 04_state_persistence.py
│   └── 05_privacy_preservation.py
├── servers/
│   ├── google_drive/
│   │   ├── __init__.py
│   │   ├── get_document.py
│   │   └── get_sheet.py
│   ├── salesforce/
│   │   ├── __init__.py
│   │   ├── update_record.py
│   │   └── query.py
│   └── slack/
│       ├── __init__.py
│       └── get_channel_history.py
├── skills/
│   ├── __init__.py
│   └── save_sheet_as_csv.py
└── client.py
```

## Requirements

- Python 3.8+
- asyncio support
- aiofiles (for async file operations)
- mcp (Model Context Protocol SDK)

## Learn More

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [Anthropic Documentation](https://docs.anthropic.com/)
- [Original Article](https://www.anthropic.com/engineering/code-execution-with-mcp)

## License

This project is provided as educational examples based on the public Anthropic article.
