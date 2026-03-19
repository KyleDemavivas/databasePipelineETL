import os, logging
from config.settings import LOG_FILE

def get_logger (name, log_file=LOG_FILE):
    
    LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs", log_file)
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

    logging.basicConfig(
        format = "%(filename)s - %(asctime)s - %(levelname)s - %(message)s \n",
        datefmt= "%m-%d-%Y %H:%M",
        filename = LOG_PATH,
        level = logging.DEBUG
    )
    
    return logging.getLogger(name)