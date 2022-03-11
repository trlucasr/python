from __future__ import print_function
import os.path
import json
import requests
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from pprint import pprint
from flask import jsonify
from flask import Flask
import json

app = Flask(__name__)

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1OZuvbuA1sIAHRtdIeK80MLDmgqP_O-nVItIUXwJZJPM'
SAMPLE_RANGE_NAME = 'Pagina1!A1:K60'
CLIENT_SECRET_FILE = r'C:\Projetos\python\Projetos\CRIE\client_secret.json'
JSON_TASK = r'C:\Projetos\python\Projetos\CRIE_API\tasks.json'

# Busca registros na Tabela do Google Sheets
def buscareg():
    creds = None

    # Verifico se existe token no path do projeto
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # Verifica se a autorização não está expirada
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # Salva a credencial para proximas requisições
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Conectando na planilha do google
    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
   
    valuesnew = []
    for a in range(1,len(values)):
        #Sobe na Plataforma?        
        if values[a][10] == "Sim"  and a > 1:                    
            valuesnew.append(values[a])

    return valuesnew

data=buscareg()

# parse file
with open(JSON_TASK, 'w') as f:
    json.dump(data, f)

with open(JSON_TASK, 'r') as myfile:
    data=myfile.read()
# parse file
obj = json.loads(data)

# obj = json.loads(data)

@app.route('/todo/getall',methods=['GET'])
def getTasks():
    return jsonify(obj)

app.run(debug=True)
