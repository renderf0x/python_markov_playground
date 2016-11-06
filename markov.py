import sys
from os import environ as env
from lib.TweetFeeder import TweetFeeder
from lib.CheapMarkov import CheapMarkov

args = sys.argv[1:]
api_key = None
if 'TWITTER_API_KEY' in env:
    api_key = env['TWITTER_API_KEY']

if len(args) < 1 or api_key == None:
    print "Make sure to set your TWITTER_API_KEY env variable, and call this function as 'python markov.py [username] [num_tweets]"
else:

    username = args[0]
    if (len(args) > 1):
        number = args[1]
    else:
        number = 20

    print "Processing for " + "@" + username + "..."
    feeder = TweetFeeder(username, api_key)
    response_texts = feeder.fetch(50)
    generator = CheapMarkov()
    generated_tweet = generator.generate_text_from_array(response_texts, 200, 4)
    print "@" + "derekryansound says:"
    print generated_tweet
    print "> created from " + str(len(response_texts)) + " tweets, split into " + str(generator.get_num_fragments()) + " fragments."
