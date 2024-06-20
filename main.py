import os
from dotenv import load_dotenv

load_dotenv('token.env')

weather_token = os.getenv("WEATHER_TOKEN_KEY")
wxpusher_token = os.getenv("WEATHER_PUSHER_TOKEN")

print(weather_token, wxpusher_token)
