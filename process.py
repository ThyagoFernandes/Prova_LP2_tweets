from contextlib import redirect_stdout
import re
with open("tweets.in", encoding="utf-8") as f:
	tweets = [line.strip() for line in f.readlines()]
	for tweet in tweets:
		searchObj = re.search( r'https:(\w.)*', tweet, re.M|re.I)
		if (searchObj):
			print ("searchObj.group() : ", searchObj.group())
		else:	
			print("nothing")
with open("tweets.out", "w", encoding="utf-8") as f:
    with redirect_stdout(f):
        print("\n".join(tweets))
  