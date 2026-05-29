import requests

def oling_ob_havo():
    api_key = "API_KEY"  # API keyni o'rniga kiritishingiz kerak
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "Toshkent",  # shahar nomini o'rniga kiritishingiz kerak
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    print(f"Hozirgi ob-havo: {data['weather'][0]['description']}")
    print(f"Havo harorati: {data['main']['temp']}°C")
    print(f"Nishonli harorat: {data['main']['feels_like']}°C")
    print(f"Havo bosimi: {data['main']['pressure']} hPa")
    print(f"Havo shamoli: {data['wind']['speed']} m/s")

oling_ob_havo()
```

API keyni o'rniga kiritishingiz kerak. OpenWeatherMap API orqali ob-havo ma'lumotlarini olish uchun API keyga ega bo'lishingiz kerak. API keyni olish uchun OpenWeatherMap veb-saytiga kirishingiz va API key so'ralishingiz kerak.
