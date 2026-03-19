import time
from sync.testConnection import run_sync, run_user_sync
from logs.logger import get_logger
from config.settings import SYNC_INTERVAL

logger = get_logger(__name__)

SYNC_JOBS = [
    run_sync,
    run_user_sync
]

def main_job_run():
    for job in SYNC_JOBS:
        print(f"Running: {job.__name__}...")
        success = job()
        if not success:
            logger.error(f"Job {job.__name__} failed.")
            print(f"{job.__name__} has failed, stopping queries.")
            return False
        print(f"Job {job.__name__} done. retrying in {SYNC_INTERVAL} seconds.")
    return True    

if __name__ == "__main__":
   try:
        while True:
            logger.info("Starting cycle.....")
            success=main_job_run()
            
            if not success:
                logger.error(f"Sync failed, retrying in {SYNC_INTERVAL} seconds.")
            else:
                logger.info(f"Sync cycle successful. Next run in {SYNC_INTERVAL} seconds.")
            
            time.sleep(SYNC_INTERVAL)       
   except KeyboardInterrupt:
       logger.info("Sync job manually stopped.")
       print("Sync stopped.")    