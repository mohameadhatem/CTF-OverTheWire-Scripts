import paramiko 
import getpass

port = 2220
host = "bandit.labs.overthewire.org"
user = "bandit10"
password = getpass.getpass("Enter Password: ") 

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port, username=user, password=password)
cmd = "base64 -d data.txt | awk '{print$4}' "
stdin, stdout, stderr = client.exec_command(cmd)
result = stdout.read().decode()
print(f"{"- "* 25}\nuser name : bandit11 \npassword : {result}\n{"- "* 25}")
