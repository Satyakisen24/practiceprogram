import os
import platform
import socket
import datetime

# Create output directory
os.makedirs("output", exist_ok=True)

hostname = socket.gethostname()
current_time = datetime.datetime.now()

report = f"""Report Date: {current_time.strftime('%Y-%m-%d %H:%M:%S')}

Hostname: {hostname}
OS: {platform.system()}
Python Version: {platform.python_version()}

Status: SUCCESS
"""

filename = f"output/report-{current_time.strftime('%Y%m%d-%H%M%S')}.txt"

with open(filename, "w") as file:
    file.write(report)

print(report)
print(f"Report saved to {filename}")