import gspread
from google.oauth2.service_account import Credentials

# Configuração básica de acesso para api
SCOPE = ["https://www.googleapis.com/auth/spreadsheets"]
CREDS = Credentials.from_service_account_file('credentials.json', scopes=SCOPE)
client = gspread.authorize(CREDS)

# INSERIR ID da planilha
SHEET_ID = "SEU_SHEET_ID"
sheet = client.open_by_key(SHEET_ID).sheet1

def get_all_machines():
    data = sheet.get_all_records()
    return data

def add_machine(machine):
    row = [
        machine["operatingSystem"],
        machine["siteName"],
        machine["deviceType"],
        machine["hostname"],
        machine["lastLoggedInUser"],
        machine["online"]
    ]
    sheet.append_row(row)
