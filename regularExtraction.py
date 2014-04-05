from bs4 import BeautifulSoup

import subprocess, sys, time, re, easyTweet, string


lines = easyTweet.timeline()[0:10]
theString = ""
for line in lines:
	match = re.search(r"(?<=at\sExceptionalStack\.)(\w)", line)
	if match:
		theString += match.group(0)
	else:
		print "no match for " + line

html = BeautifulSoup("<h1><b>"+theString).prettify()

print(html)
htmlFile = open("html.html", 'w')
htmlFile.write(html)
