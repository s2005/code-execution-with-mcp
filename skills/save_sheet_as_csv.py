"""Reusable skill: Save Google Sheet as CSV"""

import csv
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from servers import google_drive


async def save_sheet_as_csv(sheet_id: str, output_dir: str = './workspace') -> str:
    """
    Download a Google Sheet and save it as a CSV file.

    This is a reusable skill that agents can call to persist
    spreadsheet data for later processing.

    Args:
        sheet_id: The ID of the Google Sheet to download
        output_dir: Directory to save the CSV file (default: ./workspace)

    Returns:
        Path to the saved CSV file
    """
    # Fetch the sheet data
    result = await google_drive.get_sheet({'sheet_id': sheet_id})
    rows = result['rows']

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Generate output filename
    file_path = os.path.join(output_dir, f'sheet-{sheet_id}.csv')

    # Write to CSV
    if rows:
        with open(file_path, 'w', newline='') as f:
            # Get headers from first row
            headers = list(rows[0].keys())
            writer = csv.DictWriter(f, fieldnames=headers)

            writer.writeheader()
            for row in rows:
                writer.writerow(row)

    return file_path
