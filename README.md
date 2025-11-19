# Email Agent MCP Server

An MCP server that allows LLMs to draft emails using your local browser and Gmail.

## Features
- **Draft Emails**: Reads an Excel file (`Name`, `Email`) and opens Gmail compose tabs with pre-filled content.

## Installation

### Prerequisites
- Python 3.10+
- `pip`

### Local Setup
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server (for testing):
   ```bash
   python server.py
   ```

## Usage with Claude Desktop

To use this with Claude Desktop, add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "email-agent": {
      "command": "python",
      "args": ["/absolute/path/to/email_agent/server.py"]
    }
  }
}
```

Make sure to replace `/absolute/path/to/email_agent/server.py` with the actual path.

## Publishing to Smithery

1. Push this code to a public GitHub repository.
2. Register the repository on [Smithery.io](https://smithery.io).
