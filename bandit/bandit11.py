import paramiko 
import getpass

import codecs

port = 2220
host = "bandit.labs.overthewire.org"
user = "bandit11"
password = getpass.getpass("Enter Password: ") 

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port, username=user, password=password)
cmd = 'with open("data.txt", "r") as f: print(codecs.decode(f.read(), "rot_13").strip())'

stdin, stdout, stderr = client.exec_command(cmd)
result = stdout.read().decode()
print(f"{"- "* 25}\nuser name : bandit12 \npassword : {result}\n{"- "* 25}")
