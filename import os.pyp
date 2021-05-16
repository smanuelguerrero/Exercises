import os
print("\nEffective group id: ",os.getegid())
print("Effective user id: ",os.geteuid())
print("Real group id: ",os.getgid())
print("List of supplemental group ids: ",os.getgroups())
print()


#environment
print(os.environ)

#file properties

import os.path
import time

print('File :',__file__)
print('Access time:',time.ctime(os.path.getatime(__file__)))
print('Modified time:',time.ctime(os.path.getmtime(__file__)))
print('Change time:',time.ctime(os.path.getctime(__file__)))
print('Size:',os.path.getsize(__file__))

#path directory

import os.path

for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
    print('File        :', file)
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))
    

	
