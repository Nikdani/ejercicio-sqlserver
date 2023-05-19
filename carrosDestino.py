import pyodbc
import pandas as pd
from sqlalchemy import create_engine

server = 'localhost'
database = 'carrosDestino'
driver = '{ODBC Driver 17 for SQL Server}'

connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
cnxn = pyodbc.connect(connection_string)

try:
    cnxn.execute("SELECT 1")
    print("Conexión exitosa a la base de datos destino.")
except pyodbc.Error as e:
    print("No se pudo establecer la conexión a la base de datos destino:", str(e))

cnxn.close()

