import pyodbc
# Using a DSN
cnxn = pyodbc.connect('DSN=TOTVS12;UID=protheus;PWD=Senh@dm1')

print(cnxn)