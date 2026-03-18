from sqlalchemy import create_engine

#this is for placeholder only, will edit in future once needed.

POSTGRES_ENGINE = create_engine(
    'postgresql+psycopg2://user:pass@192.168.1.10:5432/dbname'
)

MYSQL_ENGINE = create_engine(
    'mysql+pymysql://user:pass@192.168.1.11:3306/dbname'
)

MSSQL_ENGINE = create_engine(
    'mssql+pyodbc://sa:Kepi-123@localhost'
)

#TODO: add and edit to correct database address, username, and password.
