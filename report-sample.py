import platform 
import os
import socket       
import datetime

hostname = socket.gethostname()
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"OS: {platform.system()}")
print(f"Hostname: {hostname}")
print(f"Report Time: {current_time}")
print(f"Version: {platform.version()}") 