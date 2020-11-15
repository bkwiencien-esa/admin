import pdb
import os

def walPurge(argo):
  ddate = argo[1]
  try:
        checkdate = dt.datetime.strptime(sys.argv[1], '%Y-%m-%d')
  except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")      
  pgdata = os.environ["PGDATA"]
  waldir = pgdata+"/pg_wal"
  statusdir = waldir+"/archive_status"
  listOfFiles=os.listdir(waldir)
  listo=[]
  datelist=[]
  for f in listOfFiles:
  	if os.path.isfile(os.path.join(waldir, f)):
      walfile = waldir+"/"+f
  		listo.append(walfile)
  return
if __name__=='__main__':
  if (len(sys.argv) < 2):
    exit("no date passed")	
  walPurge(sys.argv)  
  print("Done success as expected")