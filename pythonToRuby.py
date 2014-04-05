import subprocess
import sys

#print("In Python", sys.argv)
index = int(sys.argv[2])
if index >= len(sys.argv[1]):
	quit()
print(sys.argv[1][index])
subprocess.call(["ruby", "./rubyToShell.rb", sys.argv[1], sys.argv[2]])

