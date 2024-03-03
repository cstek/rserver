from django.shortcuts import render
from datetime import datetime
import geocoder
import requests
from django.http import HttpResponse
from django.template import loader


def temp_here(request):
    # location = geocoder.ip('me').latlng
    # endpoint = "https://api.open-meteo.com/v1/forecast"
    # api_request = f"{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m"
    # now = datetime.now()
    # hour = now.hour
    # meteo_data = requests.get(api_request).json()
    # temp = meteo_data['hourly']['temperature_2m'][hour]
    template = loader.get_template('index.html')
    city = 'random_city'
    context = {
        'temp': 111101,
        'city': city,
        }
    return HttpResponse(template.render(context, request))