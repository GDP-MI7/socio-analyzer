from twarc import Twarc
import json

#input twitter credentials
consumer_key = '*********'
consumer_secret = '*********'
access_token = '*********'
access_token_secret = '*********'

t = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)
data = []

for tweet in t.hydrate(open('../input_files/ids.txt')):
    data.append(json.dumps(tweet))

with open('output.json','w') as outfile:
    outfile.write("\n".join(data) + '\n')