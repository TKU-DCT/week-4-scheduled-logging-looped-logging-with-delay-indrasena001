import psutil
from datetime import datetime
import csv
import os
import time

def get_system_info():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # TODO: Get CPU, memory, and disk usage using psutil
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk_root = os.path.abspath(os.sep)
    disk = psutil.disk_usage(disk_root).percent
    
    return [now, cpu, memory, disk]

def write_log(data):
    file_exists = os.path.isfile("log.csv")
    with open("log.csv", "a", newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "CPU", "Memory", "Disk"])
        writer.writerow(data)

if __name__ == "__main__":
    # TODO: Repeat the log process 5 times with 10-second intervals
    for i in range(5):
        data = get_system_info()
        write_log(data)
        if i < 4:
            time.sleep(10)
