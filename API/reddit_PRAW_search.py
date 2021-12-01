import praw
import pandas as pd
#import datetime as dt
from datetime import datetime
import sys


reddit = praw.Reddit(client_id='3k7EJkOzzg6nOA', \
                     client_secret='7k5l7gPCj3D23PQYK878-D5BIKU2Ow', \
                     user_agent='searchAppAgent', \
                     username='gazagda', \
                     password='Gazagda1')

search_term='devops'
keyword='gitlab'

if (len(sys.argv)>1):
    search_term=(sys.argv[1])

if (len(sys.argv)>2):
    keyword=(sys.argv[2])

print ("Subreddit: ",search_term)
print ("Keyword: ",keyword)


subreddit = reddit.subreddit(search_term)

#resp = subreddit.search(keyword,limit=10)  previously, this g gave a generator as seen her. I converted it to a list as you can see below
resp = list(subreddit.search(keyword,limit=20))
print(resp[0].created_utc) #TODO Trying to sort this according to date

for submission in resp:
    print ("Title: ",submission.title.encode('ascii', 'ignore'))
    print ("        Reddit url :  https://np.reddit.com/r/news/comments/"+submission.id)
    print ("        permalink: ",submission.permalink)
    ts = int(submission.created_utc)
    creationDate = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print ("        Creation Date: ",creationDate)
    #print ("  Score: ",submission.score)
    #print ("  URL: ",submission.url.encode('ascii', 'ignore'))
    #print ("  Text: ",submission.selftext[:120].encode('ascii', 'ignore'))
   