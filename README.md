Microservice README

This microservice connects to a Google Sheet using the gspread library to enable CRUD functionalities. 

To use this microservice, you need to install the gspread library and have a google account or access to sheets.

. Install the gspread library by running pip install gspread

. Create a Google Cloud Platform (GCP) project, enable the Google Drive API, and create a service
account with access to the Google Sheet

. Share the Google Sheet with the email associated with the service account.

. Update the filename in gc = gspread.service_account(filename='.config/credentials.json')
with the path to your service account credentials file.

https://docs.google.com/spreadsheets/d/1fLo1K1q3lV6kPJtrF_QNQqTI6fFD-5JaVgQBUy9LHzM/edit#gid=1008797161

HERE IS THE LINK FOR MY UML DIAGRAM:

<img width="508" alt="Screenshot 2023-05-16 at 2 48 56 PM" src="https://github.com/SDL101/CS-361/assets/81109215/e7908d6e-c45f-405a-b1a6-8d3289e122ea">
