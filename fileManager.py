#! /Users/bobkwiencien/anaconda/bin/python
import pdb
import os
import sys
import datetime as dt
def removeOtioseFiles(chck,indir):
	listin = os.listdir(indir)
	for f in listin:
		if (os.path.isfile(os.path.join(indir, f))):
			ctime=os.path.getctime(indir+"/"+f)
			filetime=dt.datetime.fromtimestamp(ctime)
			if chck > filetime:
				os.remove(indir+"/"+f)
	return
def walPurge(argo):
	ddate = argo[1]
	try:
				checkdate = dt.datetime.strptime(sys.argv[1], '%Y-%m-%d')
	except ValueError:
				raise ValueError("Incorrect date format, should be YYYY-MM-DD")      
	pgdata = os.environ["PGDATA"]
	removeOtioseFiles(checkdate,pgdata+"/pg_wal")
	removeOtioseFiles(checkdate,pgdata+"/archive")
	removeOtioseFiles(checkdate,pgdata+"/archive_status")		
	return
if __name__=='__main__':
	if (len(sys.argv) < 2):
		exit("no date passed")	
	walPurge(sys.argv)  
	print("Done success as expected")