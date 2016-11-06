import sys
from os import environ as env
from lib.TweetFeeder import TweetFeeder
from lib.CheapMarkov import CheapMarkov


def run(username, api_key, num_tweets):
    print "Processing for " + "@" + username + "..."

    feeder = TweetFeeder(username, api_key)
    response_texts = feeder.fetch(50)
    generator = CheapMarkov()
    generated_tweet = generator.generate_text_from_array(response_texts, 200, 4)

    print "@" + "derekryansound says:"
    print generated_tweet
    print "> created from " + str(len(response_texts)) + " tweets, split into " + str(generator.get_num_fragments()) + " fragments."



if __name__ == '__main__':

    args = sys.argv[1:]

    api_key = None
    if 'TWITTER_API_KEY' in env:
        api_key = env['TWITTER_API_KEY']

    if len(args) < 1 or api_key == None:
        raise Exception("Make sure to set your TWITTER_API_KEY env variable, and call this function as 'python markov.py [username] [num_tweets]")

    username = args[0]
    if (len(args) > 1):
        number = args[1]
    else:
        number = 20 #defaut

    run(username, api_key, number)
