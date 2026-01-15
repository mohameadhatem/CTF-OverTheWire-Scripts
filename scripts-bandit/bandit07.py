import paramiko
import getpass

port = 2220
host = "bandit.labs.overthewire.org"
user = "bandit7"
password = getpass.getpass("Enter Password: ")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=2220, username=user, password=password)
cmd = "grep millionth data.txt | awk '{print $2}'"
stdin, stdout, stderr = client.exec_command(cmd)
result = stdout.read().decode("utf-8")
result = result.strip()
print(f"{"- "* 25}\nuser name : bandit8 \npassword : {result}\n{"- "* 25}")
client.close()
