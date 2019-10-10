import os, sys
import subprocess

JM_HOME = r'C:\JModelica.org-2.2'
setenv_path = os.path.join(JM_HOME,"setenv.bat")
setenv = subprocess.Popen(["call", setenv_path], shell=True)
setenv.wait()

p1 = subprocess.Popen(["echo", "%PATH%"], shell=True)
p1.wait()
print("--------------------------------")
print(os.path())


