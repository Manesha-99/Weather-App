from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == "POST":
        city = request.POST.get('city')
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q'+city+'&appid=46752a60b54be442fa6fd0518a9a6b34').read()
        json_data = json.loads(res)
        data = {
            "country_code": str
        }
        

    else:
        city = ''
    return render(request,'index.html', {'city': city})
