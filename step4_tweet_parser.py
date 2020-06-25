import json
import os

tweets = []
with open("tweets.json", "r") as rfile:
    for line in rfile:
        t = {}
        data = json.loads(line)
        if data['lang'] == 'en':
            t['id'] = data['id']
            t['created_at'] = data['created_at']
            t['text'] = data['text']
            t['lang'] = data['lang']
            t['user_id'] = data['user']['id']
            t['user_name'] = data['user']['name']
            t['screen_name'] = data['user']['screen_name']
            t['location'] = data['user']['location']
            tweets.append(t)
with open('output_list.json', 'w') as filehandle:
    json.dump(tweets, filehandle)
filehandle.close()
os.system("cat output_list.json | jq -c '.[]' > outputx.json")
dirname = "outputtweets"
f1 = open('outputx.json', 'r')
if not os.path.exists(dirname):
    os.makedirs(dirname)
for i, text in enumerate(f1):
    path_file = os.path.join(dirname, str(i + 1) + '.json')
    open(path_file, 'w').write(text)

for filename in os.listdir(dirname):
    if filename.endswith(".json"):
        path = dirname + "/" + filename
        command = "gsutil cp %s gs://tidal-glider-217500-files-source-1586544872" % path
        os.system(command)
