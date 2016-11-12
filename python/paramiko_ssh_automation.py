import paramiko
import sys



ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('127.0.0.1', username= sys.argv[1], 
    password = sys.argv[2])

list_of_cmds = ['date','pwd','uptime','uname']
test2=["ps -ef | awk '{print $1,$2,$3}' ",'iostat','ifconfig','lpq','netstat -rn','arp -an']

for cmd in list_of_cmds:
	stdin, stdout, stderr = ssh.exec_command(cmd)

	print stdout.readlines()


