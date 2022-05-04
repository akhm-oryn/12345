from django.http import HttpResponse
from .helper import request_data,count_k



def likes(request, website_name):

    data = request_data(website_name)
    score = data[0]['data']['children'][0]['data']['score']
    return HttpResponse(f"<html><body><h3>likes </h3>{score}</body></html>")


def awards(request, website_name):
    data = request_data(website_name)
    score = data[0]['data']['children'][0]['data']['total_awards_received']
    return HttpResponse(f"<html><body><h3>awards </h3>{score}</body></html>")


def created(request, website_name):
    data = request_data(website_name)
    score = data[0]['data']['children'][0]['data']['created_utc']
    return HttpResponse(f"<html><body><h3>created_at </h3>{score}</body></html>")


def count_keys(request,website_name):
    data = request_data(website_name)
    score = count_k(data)
    return HttpResponse(f"<html><body><h3>amount of keys </h3>{score}</body></html>")
