import requests,json

url = 'https://www.reddit.com/r/teenagers/comments/uhuitg/go_ahead_name_him/.json'
headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'saddestsempai@gmail.com'
}

response = requests.get(url, headers = headers)
data = response.json()

with open("response.txt", "w") as outfile:
    json.dump(data[0], outfile)




f = open('response.txt')


data = json.load(f)
score = data['data']['children'][0]['data']['score']
awards = data['data']['children'][0]['data']['total_awards_received']
created_utc = data['data']['children'][0]['data']['created_utc']


def count_k(d):
    keys = 0
    if type(d) == dict:
        for item in d.keys():
            if isinstance(d[item], (list,dict,tuple)):
                keys += 1
                k = count_k(d[item])
                keys += k
            else:
                keys +=1
    elif type(d) == list or type(d) == tuple:
        for item in d:
            if isinstance(item, (list,tuple,dict)):
                k = count_k(item)
                keys +=k
    return keys


