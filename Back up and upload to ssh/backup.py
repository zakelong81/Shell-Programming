#!/usr/bin/python3.5
import os, time
import tarfile
import pytz
import sys
import datetime
import subprocess

today = str(datetime.date.today())
tar_name = str(today) + ".tar.gz"

def make_tarfile():
    print("Attempting to create" + "tar.gz")
    tar = tarfile.open(tar_name, "w:gz")
    for name in list:
        tar.add(name)
    tar.close()
    print("...done")

#check if file has change in 180 second
def check_files_changed(dir):
    for rt,dirs,f in os.walk(dir):
        for fle in f:
             if time.time() - os.stat(os.path.join(rt, fle)).st_mtime < 180:
                 list.append(os.path.join(rt, fle))

if __name__ == "__main__":
    list = []
    username = sys.argv[2]
    host = sys.argv[4]
    dir = sys.argv[6]
    check_files_changed(dir)
    make_tarfile()
    p = subprocess.Popen(["scp", dir+"/"+tar_name, username+"@"+host+":./"])
    print("Attempting connect to " + host +"...done" )
    sts = os.waitpid(p.pid, 0)
    print("Upload new archive " + tar_name + "...Complete")
