import random
import subprocess

#only bash likes to run chromium for some reason
shellIndirection = [ random.choice(["./run_sh.sh", "./run_bash.sh", "./run_dash.sh"]) for x in range(random.randrange(1,10))] + [ "./run_bash.sh" ]
print(shellIndirection)

subprocess.call( shellIndirection + ["chromium", "https://www.youtube.com/watch?v=mMSHOPkcVv8"], timeout=50)