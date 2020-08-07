import tweepy
import time

auth=tweepy.OAuthHandler('API KEY','Secret') #API key & Secret
auth.set_access_token('access token ','secret') # Access Token & Secret

api=tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user =api.me()

print("Enter the hashtag/username/keyword to search:")
search=input()
print("Enter number of posts you want to Like");
nrtweets=int(input())



for tweets in tweepy.Cursor(api.search, search).items(nrtweets):
	try:
		print("Tweet Liked")
		tweets.favorite()
		time.sleep(5)
	except tweepy.TweepError as er:
		print(er.reason)
	except StopIteration:
		break
