from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render

def home(request):
    weather_data = None

    if request.method == "POST":
        city = request.POST['city']

        api_key = "4c011426892df33e87cf96b2831c3774"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        data = response.json()

        # If city found
        if data.get("cod") == 200:
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description'].title(),
                'icon': data['weather'][0]['icon'],
            }
        else:
            weather_data = {"error": "City not found!"}

    return render(request, "weather/home.html", {"weather": weather_data})
