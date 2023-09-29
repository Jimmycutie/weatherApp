import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import WeatherData
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache


index= never_cache(TemplateView.as_view(template_name="index.html"))

@api_view(['POST'])
def get_weather(request):
    location = request.data.get('location')
    
   
    api_key = 'd516f8ec659e68ff466dd566f0758fed'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'

    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            temperature = round(data['main']['temp'] - 273.15)
            humidity = data['main']['humidity']
            conditions = data['weather'][0]['description']
            icons = data['weather'][0]['icon']
            wind = data['wind']['speed']

            # Save data to the database
            WeatherData.objects.create(
                location=location,
                temperature=temperature,
                humidity=humidity,
                conditions=conditions,
            )

            return Response({
                'location': location,
                'temperature': temperature,
                'humidity': humidity,
                'conditions': conditions,
                'icons':icons,
                'wind': wind
            })
        else:
            return Response({'error': 'Unable to fetch weather data'}, status=response.status_code)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
