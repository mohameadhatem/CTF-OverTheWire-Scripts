import paramiko


host = "bandit.labs.overthewire.org"
port = 2220
user_name = "bandit2"
password = "263JGJPfgU6LtdEvgfWU1XP5yac29mFx"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(host, port, username =user_name, password =password)
cmd = "cat ./--spaces\\ in\\ this\\ filename--"

stdin, stdout, stderr = client.exec_command(cmd)

result = stdout.read().decode('utf-8')


print(f"{"- "* 25}\nuser name : bandit3 \npassword : {result}\n{"- "* 25}")

