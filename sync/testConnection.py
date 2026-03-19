import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import text
from config.connections import MSSQL_ENGINE

with MSSQL_ENGINE.connect() as connection:
    result = connection.execute(text("select * from user_account"))
    
    for row in result:
        print("username: ", row.user_namefl)