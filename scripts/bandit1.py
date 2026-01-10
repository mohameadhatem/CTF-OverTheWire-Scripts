import paramiko

host = "bandit.labs.overthewire.org"
user = "bandit1"
password = "ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If"
port = 2220

client = paramiko.SSHClient()
# To Create Finger Print Key
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, password=password)
cmd = "cat ./-"

sin, sout, serr = client.exec_command(cmd)
result = sout.read().decode("utf-8")
print(f"{"- "* 25}\nuser name : bandit2 \npassword : {result}\n{"- "* 25}")
