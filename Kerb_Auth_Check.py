import subprocess
from subprocess import Popen, PIPE

def auth_kinit (username, password):
	auth = Popen(['kinit', username], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	auth.stdin.write('%s\n' % password)
	auth.wait()
	return does_ticket_exist(username)

def does_ticket_exist(username):
    ## This will have to be update to the relative path, no way currently of seeing tmp
    a = Popen(['grep', "-nr" ,'Scott', "/Users/Scott/Desktop"]).communicate()
    print a
    x,y = a
    print x
    print y
    if a > 0:
        return False
    else:
        return False



