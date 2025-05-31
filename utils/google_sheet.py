import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_spreadsheet():
    # Configuration de l'accès Google Sheets
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(credentials)

    # Ouvre ta feuille Google Sheets
    SHEET_URL = "https://docs.google.com/spreadsheets/d/1Rxz2-dF4XUuCsknYeigbk_EONdB1fRHWcKgM3Mw35VE/edit#gid=0"
    spreadsheet = client.open_by_url(SHEET_URL)
    return spreadsheet

