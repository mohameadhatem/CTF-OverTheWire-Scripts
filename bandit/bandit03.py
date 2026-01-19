import paramiko
import getpass

host = "bandit.labs.overthewire.org"
port = 2220
user = "bandit3"
password = getpass.getpass("Enter Password: ")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(host, port, username =user, password =password)
cmd = "cat inhere/...Hiding-From-You"

stdin, stdout, stderr = client.exec_command(cmd)

result = stdout.read().decode('utf-8')


print(f"{"- "* 25}\nuser name : bandit4 \npassword : {result}\n{"- "* 25}")
