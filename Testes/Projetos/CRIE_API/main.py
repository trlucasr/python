from __future__ import print_function
import os.path
import re
import requests
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from pprint import pprint
from flask import Flask, render_template

# instancia flask no app
app = Flask(__name__)

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1OZuvbuA1sIAHRtdIeK80MLDmgqP_O-nVItIUXwJZJPM'
SAMPLE_RANGE_NAME = 'Pagina1!A1:K60'
CLIENT_SECRET_FILE = r'C:\Projetos\python\Projetos\CRIE\client_secret.json'

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

#Instancia pagina do Crie com as informações do Sheets
@app.route("/crie")
def pagecrie():        
    return render_template("crie.html", len = len(buscareg()) , registros = buscareg())


if __name__ == '__main__':   
    app.run(use_reloader = True, debug = True)