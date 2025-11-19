from fastmcp import FastMCP
import pandas as pd
import webbrowser
import urllib.parse
import time
import os

# Initialize the MCP server
mcp = FastMCP("Email Agent")

@mcp.tool()
def draft_emails(excel_path: str) -> str:
    """
    Reads an Excel file and opens Gmail compose tabs for each recipient.
    
    Args:
        excel_path (str): Absolute path to the Excel file containing 'Name' and 'Email' columns.
    """
    if not os.path.exists(excel_path):
        return f"Error: File '{excel_path}' not found."

    try:
        df = pd.read_excel(excel_path)
    except Exception as e:
        return f"Error reading Excel file: {e}"

    if 'Name' not in df.columns or 'Email' not in df.columns:
        return "Error: Excel file must contain 'Name' and 'Email' columns."

    results = []
    for index, row in df.iterrows():
        name = row['Name']
        email_address = row['Email']
        
        if pd.isna(name) or pd.isna(email_address):
            continue

        subject = "Hello from Python!"
        body = f"Hello {name},\n\nThis is a personalized email drafted by the Email Agent MCP server."

        # URL encode parameters
        params = {
            'view': 'cm',
            'fs': '1',
            'to': email_address,
            'su': subject,
            'body': body
        }
        query_string = urllib.parse.urlencode(params)
        url = f"https://mail.google.com/mail/?{query_string}"

        # Open in browser
        webbrowser.open(url)
        results.append(f"Drafted email for {name} ({email_address})")
        time.sleep(0.5)

    return "\n".join(results)

if __name__ == "__main__":
    mcp.run()
