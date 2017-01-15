import subprocess


proc = subprocess.Popen(['ssh','medhamalgaonkar@10.0.0.7'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
proc.communicate('Atmaram123\n')

#proc.stdin.write("Atmaram123\n")
#proc.stdin.write("ls -ltr\n")









