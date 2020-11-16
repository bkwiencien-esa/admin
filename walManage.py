#! /Users/bobkwiencien/anaconda/bin/python
import pdb
import os
import sys
import datetime as dt

def walPurge(argo):
	ddate = argo[1]
	#pdb.set_trace()
	try:
				checkdate = dt.datetime.strptime(sys.argv[1], '%Y-%m-%d')
				print("Checkdate = ".format(checkdate))
	except ValueError:
				raise ValueError("Incorrect date format, should be YYYY-MM-DD")      
	pgdata = os.environ["PGDATA"]
	waldir = pgdata+"/pg_wal"
	archivedir = pgdata+"/archive"
	statusdir = waldir+"/archive_status"
	listOfWalFiles=os.listdir(waldir)
	for f in listOfWalFiles:
		if (os.path.isfile(os.path.join(waldir, f))):
			ctime=os.path.getctime(waldir+"/"+f)
			filetime=dt.datetime.fromtimestamp(ctime)
			print("checkdate {}".format(checkdate))
			print("filetime {}".format(filetime))
			if checkdate > filetime:
				print("i will delete the bitch")
				os.remove(waldir+"/"+f)
	return
if __name__=='__main__':
	if (len(sys.argv) < 2):
		exit("no date passed")	
	walPurge(sys.argv)  
	print("Done success as expected")