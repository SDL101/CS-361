from google_sheet_api import get_credentials, get_sheet, load_data

# Replace with the correct path to the credentials file
credentials_path = "credentials.json"

# Get the Google API credentials and the sheet
creds = get_credentials(credentials_path)
sheet = get_sheet(creds, "Median Home Prices by ZIP Code")

# Load the data from the Google Sheet
df = load_data(sheet)
print(df)