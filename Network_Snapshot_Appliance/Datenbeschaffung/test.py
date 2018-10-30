#!/usr/bin/python3.5
#Testfile

text = getNetmask()
print(text)



def getNetmask():
    cmd = "['ifconfig']"
    result = execCommand(cmd)
    netmask = result
    return netmask
 
 
def execCommand(cmd):
    result = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    retVal = result.stdout.decode('utf-8')
    
    return retVal