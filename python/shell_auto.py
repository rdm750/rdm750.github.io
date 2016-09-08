import os

var=os.popen('ifconfig')
var_b=var.read()
print var_b
var.close()






