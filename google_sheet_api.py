import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

def get_credentials(credentials_path):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
    return creds

def get_sheet(creds, sheet_name):
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1
    return sheet

def load_data(sheet):
    data = sheet.get_all_values()
    df = pd.DataFrame(data[1:], columns=data[0])
    return df

def update_data(sheet, row_index, column_index, new_value):
    sheet.update_cell(row_index, column_index, new_value)

def append_data(sheet, data):
    sheet.append_row(data)
