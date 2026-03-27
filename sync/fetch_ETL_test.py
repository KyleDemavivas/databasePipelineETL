import sys, os, warnings

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import text
from sqlalchemy.exc import SAWarning
from config.connections import TEST_ENGINE, MSSQL_ENGINE
from logs.logger import get_logger

warnings.filterwarnings('ignore', category=SAWarning)

logger = get_logger(__name__)

def run_sync():
    try:
        with TEST_ENGINE.connect() as conn:
            result = conn.execute(
                text(
                    "SELECT lot + '-' + serial FROM ftData"
                )
            ).fetchone()
            
            print(f"{result}")
            logger.info("Fetch Successful!")
            return result
        
    except Exception as e:
        
        logger.error(f": {e}")
        return False      
    
def load_data(data):
    try:
        with MSSQL_ENGINE.connect() as conn:
            result = conn.execute(
                text(
                    f"INSERT INTO table_name(column_name) VALUES ({data})"
                )
            )
            
            conn.commit()
            logger.info("Data inserted!")
            print("Data inserted!")

    except Exception as e:
        
        logger.error(f": {e}")
        
        print("Error has occured, check logs for details.")              

run_sync()