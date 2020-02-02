import requests
from django.http import HttpResponse
from django.shortcuts import render

POCKEMON_URL = 'https://pokeapi.co/api/v2/'


SIMPLE_TEMPLATE = """
<html>
<head>
    <title>Pokemon</title>
</head>
<body>
    <a href="/list">data from another API in internet</a>
</body>
</html>
"""


def health_check(request):
    return HttpResponse("ok")


def index_func(request):
    return HttpResponse(SIMPLE_TEMPLATE)


def list_func(request):
    response = requests.get(f'{POCKEMON_URL}/type/3')
    response_list = [(i, p['pokemon']['name'], p['pokemon']['url'])
                     for i, p in enumerate(response.json()['pokemon'], start=1)]
    return render(request, 'list.html', {'value': response_list})