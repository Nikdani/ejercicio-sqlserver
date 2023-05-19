import pyodbc
from sqlalchemy import create_engine

server = 'localhost'
database = 'Nicodbsqlserver'
driver = '{ODBC Driver 17 for SQL Server}'

connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
cnxn = pyodbc.connect(connection_string)


try:
    cnxn.execute("SELECT 1")
    print("Conexión exitosa a la base de datos origen.")
except pyodbc.Error as e:
    print("No se pudo establecer la conexión a la base de datos origen:", str(e))


