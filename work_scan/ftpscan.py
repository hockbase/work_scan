# coding: utf-8
# by liuzeming

import  ftplib

def ftpscan(host):
	f = ftplib.FTP(host)
	print f.getwelcome()
	print f.login()
	print f.dir()
	f.quit()



ftpscan("115.231.81.231")