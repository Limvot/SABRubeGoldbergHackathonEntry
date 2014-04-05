#from bs4 import BeautifulSoup

import subprocess, sys, time, easyTweet, string

def generateJava(names):
	names.reverse()
	javaCode = "public class ExceptionalStack {\n"
	javaCode += "    public static void main(String[] args) throws Exception {\n"
	javaCode += "         " + names[0] + "();\n"
	javaCode += "    }\n"
	for i in range(len(names)):
		javaCode += "    public static void " + names[i] + "() throws Exception { \n"
		javaCode += "        " + ("throw new Exception" if i == len(names)-1 else names[i+1]) + "();\n"
		javaCode += "    }\n"
	javaCode += "}"
	return javaCode

def namify(character):
	if character in string.digits:
		return ""
	if character == " ":
		return "_"
	if character == ".":
		return ""
	return character

names = map(lambda x: "".join(map(lambda y: namify(y), x)), easyTweet.timeline()[0:10])
print names
javaCode = generateJava(names)
print(javaCode)
file = open('ExceptionalStack.java', 'w')
file.write(javaCode)
file.close()

#subprocess.Popen(["javac", "ExceptionalStack.java"]).wait()
subprocess.call(["javac", "ExceptionalStack.java"])
proc = subprocess.Popen(["java", "ExceptionalStack"], stderr=subprocess.PIPE)
proc.wait()
result = []
# for line in iter(proc.stdout.readline,''):
for line in proc.stderr.readlines():
	print(line)
	line = line.decode(encoding='UTF-8')
	if line == '':
		break
	print(line)
	result.append(line)
for toTweet in result[1:-1]:
	easyTweet.tweet(toTweet[0: 140 if len(toTweet) > 140 else len(toTweet)])



#print(BeautifulSoup("<p>Some<b>bad<i>HTML").prettify())
