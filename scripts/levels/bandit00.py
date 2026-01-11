import paramiko

host = "bandit.labs.overthewire.org"
user_name = "bandit0"
password = "bandit0"
port = 2220

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user_name, password=password)
cmd = "grep password readme |awk '{print $8}'"
stdin, stdout, stderr = client.exec_command(cmd)
result =  stdout.read().decode()
print(f"{"- "* 25}\nuser name : bandit1 \npassword : {result}\n{"- "* 25}")
client.close()
