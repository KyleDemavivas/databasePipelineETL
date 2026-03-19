import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SYNC_INTERVAL = 60
TIMEZONE = 'Asia/Manila'
LOG_FILE = os.pathjoin(BASE_DIR, 'logs/sync.log')
STATE_FILE = os.pathjoin(BASE_DIR, 'state/db_state.json')

#WAG PALITAN BABANATAN KITA