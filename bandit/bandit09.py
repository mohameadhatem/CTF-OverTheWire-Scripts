import paramiko 
import getpass

port = 2220
host = "bandit.labs.overthewire.org"
user = "bandit9"
password = getpass.getpass("Enter Password: ")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port, username=user, password=password)

cmd = "strings data.txt | grep -oE '[A-Za-z0-9]{32}' | head -n 1"
stdin, stdout, stderr = client.exec_command(cmd)
result = stdout.read().decode() 
print(f"{"- "* 25}\nuser name : bandit10 \npassword : {result}\n{"- "* 25}")