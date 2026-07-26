import datetime
import os
import socket
import platform

hostname = socket.gethostname()
os_info = os.uname() if hasattr(os, 'uname') else None
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Python Version: {platform.python_version()}")
print(f"Hostname: {hostname}")
print(f"Report Date: {current_time}")
print(f"OS Info: {os_info}")