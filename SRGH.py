import subprocess

#spawn Ezma in a new process so people have something pretty to look at while we work
print("Watching Ezma")
proc = subprocess.Popen(["python", "watchEzma.py"])

#clean up our messes
print("Removing old Java stuff")
subprocess.call(["rm", "ExceptionalStack.class", "ExceptionalStack.java"])

# Let's get hello world from beautifulTextExtraction, which
# Scrapes text that starts with each letter from the Wikipedia
# article South African labour law, the longest non-list Wikipedia
# has. It then saves these sentences as tweets on the MiloIgnis account.
# BeautifulSoup - used for text exctraction - and python-twitter - used for tweeting -
# are python2, so use python 2.
print("Calling beautifulTextExtraction")
subprocess.call(["python2", "beautifulTextExtraction.py"])

# let's make a ExceptionalStack. Since this pulls the sentences
# from the MiloIgnis twitter, it also needs to be python2.
print("Calling exceptionalStack")
subprocess.call(["python2", "exceptionalStack.py"])

# ExceptionalStack saves it's stack on Twitter again
# Now we extract it into a word
print("Calling regularExtraction")
subprocess.call(["python2", "regularExtraction.py"])

# regularExtraction saves it's extracted text as html, so start up Python's
# simple demo webserver to serve the current directory
# and point chromium to it
print("Watching Ezma")
proc = subprocess.Popen(["python2", "-m", "SimpleHTTPServer", "8080"])
subprocess.call(["chromium", "http://localhost:8080/html.html"])


#clean up our messes
print("Cleaning Java stuff")
subprocess.call(["rm", "ExceptionalStack.class", "ExceptionalStack.java"])