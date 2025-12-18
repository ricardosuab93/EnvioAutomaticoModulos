import os
import pyodbc
from dotenv import load_dotenv

# Carga variables desde .env
load_dotenv()


def get_connection():
    """
    Retorna una conexión a SQL Server usando variables de entorno
    """
    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_DATABASE")
    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    if not all([server, database, username, password]):
        raise RuntimeError("Variables de entorno de BD incompletas")

    conn_str = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password}'
    )

    return pyodbc.connect(conn_str)