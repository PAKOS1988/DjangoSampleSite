from django.shortcuts import render
import requests
from weather.models import City
from weather.forms import CityForm

# Create your views here.
def index(request):
    APIK='2049a16b5197b3382fde33173d1ac813'
    urls= 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + APIK
    if (request.method=='POST'):
        form = CityForm(request.POST)
        form.save()
    form = CityForm()

    cities = City.objects.all()
    print('города имеющиеся в списке')
    print(cities)
    all_cities = []
    for city in cities:
        res = requests.get(urls.format(city.name)).json()
        print(res)
        city_info={
            'city':city.name,
            'temp':res['main']['temp'],
            'humid':res['main']['humidity'],
            'icon':res['weather'][0]['icon'],
            'cloud_spd':res['wind']['speed'],
        }
        all_cities.append(city_info)
    contex = {'all_info':all_cities, 'form':form}

    return render(request, 'weather/index.html', contex)