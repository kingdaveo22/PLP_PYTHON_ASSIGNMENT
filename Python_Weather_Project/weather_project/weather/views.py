import requests
from django.shortcuts import render
from .forms import CityForm

def weather_view(request):
    api_key = '9f7197a80a07f7d37e53f5afed6c9d4f'  # Replace with your valid API key
    weather_data = None
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {'message': 'City not found'}
            print(response.json())  # Print the response to debug
    else:
        form = CityForm()

    context = {
        'form': form,
        'weather_data': weather_data,
    }
    return render(request, 'weather/weather.html', context)
