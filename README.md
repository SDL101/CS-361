Microservice README

This microservice connects to a Google Sheet using the gspread library to enable CRUD functionalities. 

To use this microservice, you need to install the gspread library and have a google account or access to sheets.

. Install the gspread library by running pip install gspread

. Create a Google Cloud Platform (GCP) project, enable the Google Drive API, and create a service
account with access to the Google Sheet

. Share the Google Sheet with the email associated with the service account.

. Update the filename in gc = gspread.service_account(filename='.config/credentials.json')
with the path to your service account credentials file.

