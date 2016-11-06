# Python Markov Playground

A simple example of parsing a Twitter feed and spitting out a generated tweet via Markov chains.

## Running

This requires having a Twitter API App setup on their dev platform.

```sh
# 1) Clone, install python requests library
pip install requests
# 2) Set a base-64 encoded auth string as TWITTER_API_KEY (See Twitter API App docs)
export TWITTER_API_KEY=[KEY]
# 3) Run against a Twitter account, optionally speficying the number of tweets to pull as a base
python markov.py derekryansound 200
```
## Structure

While the `markov.py` is the runnable script, the actual processing is in `lib/CheapMarkov.py` and `lib/TweetFeeder.py`
