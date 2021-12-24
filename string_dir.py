import subprocess

 
p = subprocess.run(['ls', '-la'])

print(p.returncode)