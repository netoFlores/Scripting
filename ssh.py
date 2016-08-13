import pxssh
import getpass
try:                                                            
	options  = dict(StricHostKeyChecking="no",)
	s = pxssh.pxssh(options)
	hostname = raw_input('hostname: ')
	username = raw_input('username: ')
	password = getpass.getpass('password: ')
	s.PROMPT= 'SSH> '
	s.login (hostname, username, password, auto_prompt_reset=False)
	print 'Login successful'
	s.sendline ('uptime')  # run a command
	print s.before 
	s.logout()
except pxssh.ExceptionPxssh, e:
	print "pxssh failed on login."
	print str(e)
