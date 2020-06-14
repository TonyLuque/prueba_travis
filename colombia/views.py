from django.http import HttpResponse
import json

def top_ten_cities(request):
    data = {
                'status':'ok',
                'top_ten':[
                    {'city':'bogota',
                    'cases':45983,
                    'death':7884,
                    'recovered':4883},
                    {'city':'cali',
                    'cases':74808,
                    'death':8594,
                    'recovered':7439},
                    {'city':'medellin',
                    'cases':56980,
                    'death':5349,
                    'recovered':9320},
                    ]
            }
    return HttpResponse(json.dumps(data))

def top_ten(request):
    data = {
        'status':'ok',
        'top_ten':[
            {'department':'antioquia',
                'cases':739473,
                'death':73847,
                'recovered':34355},
            {'department':'cundinamarca',
                'cases':30483,
                'death':8484,
                'recovered':8473},
            {'department':'boyaca',
                'cases':34003,
                'death':4839,
                'recovered':24980},
            ]
    }
    return HttpResponse(json.dumps(data))

def city(request, city):
    data = {
        'status':'ok',
        'city':city,
        'cases':38473,
        'death':4338,
        'recovered':3447
    }
    return HttpResponse(json.dumps(data))
