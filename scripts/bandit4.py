import paramiko
from paramiko.client import AutoAddPolicy

user = "bandit4"
password = "2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ"
port = 2220
host = "bandit.labs.overthewire.org"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port,username=user, password=password)
cmd = ("cat inhere/./-file07")
stdin, stdout, stderr = client.exec_command(cmd)
result = stdout.read().decode("utf-8")
print(f"{"- "* 25}\nuser name : bandit5 \npassword : {result}\n{"- "* 25}")