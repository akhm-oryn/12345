from django.http import HttpResponse
import requests
from test import count_k


def get_params(query, data):
    params = ""
    if query == "likes":
        params = data['data']['children'][0]['data']['score']
    elif query == "awards":
        params = data['data']['children'][0]['data']['total_awards_received']
    elif query == "created":
        params = data['data']['children'][0]['data']['total_awards_received']
    elif query == "count":
        params = count_k(data)
    return params


def get_awards(request, pk):
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'saddestsempai@gmail.com'
    }


    response = requests.get(
        f"https://www.reddit.com/{pk}.json",
        headers=headers
    )


    query = request.GET.get("search")


    data = response.json()[0]
    params = get_params(query=query, data=data)
    return HttpResponse(f"<html><body>{query}:{params}</body></html>")







    # score = data['data']['children'][0]['data']['score']
    # awards = data['data']['children'][0]['data']['total_awards_received']
    # created_utc = data['data']['children'][0]['data']['created_utc']

    #
    # with open("response.json", "w") as outfile:
    #     json.dump(data[0], outfile)
