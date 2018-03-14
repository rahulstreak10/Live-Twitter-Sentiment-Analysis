from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey="IFHlbeVAJqGbHrYemmhot9MXS"
csecret="SueG2VO3QWWvdOXTCfNLaY8dTJIiJZTQhaNszfuQqBfynJSBM2"
atoken="728278320454979585-XHr1VuIkRSP0gQ0ZHlIHctzylQ7wIiR"
asecret="MKmorVBWO8gR3dK33ZJFvfN0r9TCY7Lq8V4KjNOOWLhx7"

class listener(StreamListener):
	def on_data(self, data):
		try:
			print("started here")
			all_data=json.loads(data)
			tweet = all_data["text"]
			print ("Tweet:",tweet)
			sentiment_value, confidence = s.sentiment(tweet)
			print(tweet, sentiment_value, confidence)

			if confidence*100 >= 80:
				output = open("twitter-out.txt","a")
				output.write(sentiment_value)
				output.write('\n')
				output.close()

			return True
		except:
			return True

	def on_error(self, status):
		print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["obama"])