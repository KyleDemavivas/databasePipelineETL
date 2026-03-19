import sys, os, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import text
from config.connections import MSSQL_ENGINE
from logs.logger import get_logger

logger = get_logger(__name__)

def run_sync():
    try:
        with MSSQL_ENGINE.connect() as connection:
            result = connection.execute(text("select * from user_account")).fetchall()
        
            for row in result:
                print("username: ", row.user_namefl)
                
            logger.info("Fetch is successful!")      
            
    except Exception as e:
        logger.error(f": {e}")
        print("Something went wrong. Check log files for details")