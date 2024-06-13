import json
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def api_view(request, *args, **kwargs):
    print(request.body)
    data = json.loads(request.body)
    print(data)
    
    #data = {
    #    'Nom':'ESCANOR',
    #    'language':'python'
    #}
    data['headers'] = dict(request.headers)
    data['params'] = dict(request.GET)
    data['post_params'] = dict(request.POST)
    data['content_type'] = request.content_type
    return JsonResponse(data)