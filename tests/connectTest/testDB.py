import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC DRIVER 17 FOR SQL SERVER};"
    "SERVER=localhost;"
    "DATABASE=prod_traceability;"
    "UID=sa;"
    "PWD=Kepi-123;"
)
print("Connected!")