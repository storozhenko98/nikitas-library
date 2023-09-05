import requests
import os
import subprocess
from datetime import datetime

def init_directory():
    library_dir = os.path.expanduser("~/nikita_library")
    if not os.path.exists(library_dir):
        os.makedirs(library_dir)
    return library_dir

def download_library(ssh_address, library_dir):
    cmd = f'scp -r ubuntu@{ssh_address}:~/server_library {library_dir}/'
    subprocess.run(cmd, shell=True)

def upload_library(ssh_address, library_dir):
    cmd = f'scp -r {library_dir} ubuntu@{ssh_address}:~/'
    subprocess.run(cmd, shell=True)

def log_activity(action, library_dir):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(os.path.join(library_dir, 'activity_log.txt'), 'a') as f:
        f.write(f"{timestamp} - {action}\n")

library_dir = init_directory()


print('''
       .--.                   .---.
   .---|__|           .-.     |~~~|
.--|===|--|_          |_|     |~~~|--.
|  |===|  |'\     .---!~|  .--|   |--|
|%%|   |  |.'\    |===| |--|%%|   |  |
|%%|   |  |\.'\   |   | |__|  |   |  |
|  |   |  | \  \  |===| |==|  |   |  |
|  |   |__|  \.'\ |   |_|__|  |~~~|__|
|  |===|--|   \.'\|===|~|--|%%|~~~|--|
^--^---'--^    `-'`---^-^--^--^---'--' 
      
''')

print("Welcome to Nikita's Library!")
print("")
print("Getting SSH Address...")

ssh_address = requests.get('https://personal-projects.a2hosted.com/home-ssh').text

print("Got it! Library Address is: " + ssh_address)

decision = input('''
What would you like to do?
[1] Download Library
[2] Upload Library
[3] Exit
                 
''')

if decision == "1":
    print("Downloading library...")
    download_library(ssh_address, library_dir)
    log_activity("Downloaded Library", library_dir)
    print("Library downloaded!")
elif decision == "2":
    print("Uploading library...")
    upload_library(ssh_address, library_dir)
    log_activity("Uploaded Library", library_dir)
    print("Library uploaded!")
elif decision == "3":
    print("Exiting...")
else:
    print("Invalid choice.")
