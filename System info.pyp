import os
import platform as pfm
import sys

def endline():
  print('*--------------------*')
  
print("OS info: ",os.name)
endline()
print("System info: ",pfm.system)
endline()
print("Version: ",sys.version)
endline()
print("Release info: ",pfm.release())
endline()
print("List Directory: ",os.listdir())
endline()
print(os.environ)
endline()
print(os.environ['HOME'])
endline()
print(os.environ['PATH'])
endline()
