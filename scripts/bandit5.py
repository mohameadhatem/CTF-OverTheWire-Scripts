import paramiko

port = 2220
host = "bandit.labs.overthewire.org"
user = "bandit5"
password = "4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port, username=user, password=password)
cmd = "cat inhere/maybehere07/.file2"
stdin, stdout, stderr = client.exec_command(cmd)
result = stdout.read().decode("utf-8")
result = result.strip()
print(f"{"- "* 25}\nuser name : bandit5 \npassword : {result}\n{"- "* 25}")
