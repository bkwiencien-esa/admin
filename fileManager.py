#! /Users/bobkwiencien/anaconda/bin/python
import pdb
import os
import sys
import datetime as dt

def walPurge(argo):
	ddate = argo[1]
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
			if checkdate > filetime:
				os.remove(waldir+"/"+f)
	listOfArchiveFiles=os.listdir(archivedir)			
	for ff in listOfArchiveFiles:
		if (os.path.isfile(os.path.join(archivedir, ff))):
			ctime=os.path.getctime(archivedir+"/"+ff)
			filetime=dt.datetime.fromtimestamp(ctime)
			if checkdate > filetime:
				os.remove(archivedir+"/"+ff)			
	return
if __name__=='__main__':
	if (len(sys.argv) < 2):
		exit("no date passed")	
	walPurge(sys.argv)  
	print("Done success as expected")