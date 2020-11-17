#!/bin/bash
set -e
export PATH=.:$PATH
PGDATA=/usr/local/var/postgres
BACKUP=/usr/local/Cellar/postgresql/12.1/bin/pg_basebackup
DIRBASE=/Users/bobkwiencien/backups
MKDIR=/bin/mkdir
WALMANAGE=fileManager.py
findDir()  {
a=`date "+%Y-%m-%d"`
diro=$DIRBASE/$a
if [ -f $diro ]; then
:
else
  $MKDIR $diro
fi
}
findDir
$BACKUP -D $diro -Ft -z -X stream
$WALMANAGE $a