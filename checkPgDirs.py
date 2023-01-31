#check if postgres dirs are present, if not make before attempting to start db
#reasoning:
#   postgres requires some directories that at the moment are empty
#   this is an issue when attempting to deploy the project with docker-compose
#   on another machine using github as github doesn't track empty directories
#       i attempted to have github track by using .gitkeep in these empty dirs
#       but this only caused postgres to error out due to attempting to read these
#       .gitkeep files
#       example errors
#       db_1          | 2023-01-31 08:49:49.658 UTC [1] LOG:  could not open directory "pg_tblspc/.gitkeep/PG_13_202007201/pgsql_tmp": Not a directory
#       db_1          | 2023-01-31 08:49:49.659 UTC [1] LOG:  could not open directory "pg_tblspc/.gitkeep/PG_13_202007201": Not a directory

#workaround
#   build docker-compose service that runs this script and checks for the missing
#   dirs. if they are missing, create before docker attempts to start pg db
from pathlib import Path
import os
dirList = open('pgdirs.list')
dirs = dirList.readlines()
rootDir = "./data/db"
print("Checking the following(and making if necessary)")
for directory in dirs:
    path = os.path.join(rootDir,directory)
    path = path.strip()
    print(path)
    Path(path).mkdir(exist_ok=True)
