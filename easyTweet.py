import twitter

consumer_key = "j8ebfyGowdGZi0E76ZOKDxFRI"
consumer_secret = "OvEck9u8kVZpdSBKUty2k8R6ZPQVEFlg7Wf6QJPM2lknZ4JH8Y"
access_key = "2429424710-D2D6vkNrMKfvBpxnhNCv5JIKifDSJ9L7YRlAXyE"
access_secret = "YXrVFjb9oDinVyJQDejBi4oKWbgwP7pQU96yvfRaI2JnF"

api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
					access_token_key=access_key, access_token_secret=access_secret)

def tweet(tweet):
	api.PostUpdate(tweet)

def timeline():
	return [status.text for status in api.GetUserTimeline("MiloIgnis")]


def main():
	print timeline()

if __name__ == "__main__":
	main()