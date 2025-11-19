import pandas as pd
import webbrowser
import urllib.parse
import sys
import time

def draft_emails(excel_file):
    """
    Reads an Excel file and opens Gmail compose tabs for each recipient.
    
    Args:
        excel_file (str): Path to the Excel file.
    """
    try:
        df = pd.read_excel(excel_file)
    except FileNotFoundError:
        print(f"Error: File '{excel_file}' not found.")
        return
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return

    # Check if required columns exist
    if 'Name' not in df.columns or 'Email' not in df.columns:
        print("Error: Excel file must contain 'Name' and 'Email' columns.")
        return

    print(f"Found {len(df)} recipients. Opening browser tabs...")

    for index, row in df.iterrows():
        name = row['Name']
        email_address = row['Email']
        
        if pd.isna(name) or pd.isna(email_address):
            print(f"Skipping row {index}: Missing Name or Email")
            continue

        subject = "Hello from Python!"
        body = f"Hello {name},\n\nThis is a personalized email drafted by a Python script. Waiting for you to hit send!"

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

        print(f"Drafting email for {name} ({email_address})...")
        webbrowser.open(url)
        
        # Small delay to ensure browser handles requests gracefully
        time.sleep(1)

    print("All drafts opened. Please review and send them in your browser.")

if __name__ == "__main__":
    file_path = 'process_data.xlsx'
    draft_emails(file_path)
