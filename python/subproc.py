import subprocess


proc = subprocess.Popen(['ssh','user@192.168.1.1'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
proc.communicate('Atmaram123\n')

#proc.stdin.write("password\n")
#proc.stdin.write("ls -ltr\n")









