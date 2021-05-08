import glob
import os

files = glob.glob("*.txt")
files.sort(key=os.path.getmtime)

print("\n".join)


#directory listing

import glob
import os
from stat import S_ISREG, ST_CTIME, ST_MODE
import sys
import time

dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

data = (os.path.join(dir_path,fn) for fn in os.listdir(dir_path))
data = ((os.stat(path),path) for path in data)

data = ((stat[ST_CTIME],path) for stat, path in data if S_ISREG(stat[ST_MODE]))

for cdate, path in sorted(data):
  print(time.ctime(cdate),os.path.basename(path))
