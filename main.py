import os, time
from sync.testConnection import run_sync

while True:
    run_sync()
    print("Running...")
    time.sleep(60)