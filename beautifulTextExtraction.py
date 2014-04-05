import urllib
from bs4 import BeautifulSoup
import re
import requests
import easyTweet
import time, sys, random

random.seed()

url = "https://en.wikipedia.org/wiki/South_African_labour_law"
searchString = "HelloWorld"

def findSentenceStartingWith(letter, text):
	results = re.findall(r"(?<=\s)(" + letter + r"(\w|\s)*\.\s)", text)
	textResults = []
	for result in results:
		textResults.append(result[0])
	return textResults

opener = urllib.FancyURLopener({})
html = opener.open(url).read()
article = BeautifulSoup(html)
articleText = article.get_text()

sentences = []
i = 0
for character in searchString:
	#print(findSentenceStartingWith(i, articleText))
	sentenceOptions = findSentenceStartingWith(character,articleText)
	sentences.append(sentenceOptions[(i+random.randint(0, sys.maxint))%len(sentenceOptions)])
	i += 1

# print(sentences)
# sys.exit(0);

print(sentences)
for sentence in sentences:
	toTweet = str(time.clock())+sentence
	toTweet = toTweet[0: 140 if len(toTweet) > 140 else len(toTweet)]
	easyTweet.tweet(toTweet)




 