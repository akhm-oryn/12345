import requests
def request_data(website_name):
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'saddestsempai@gmail.com'
    }

    response = requests.get('https://www.reddit.com/' + website_name + '.json', headers = headers)

    return response.json()


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