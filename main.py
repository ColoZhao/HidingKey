import os
from dotenv import load_dotenv

load_dotenv('token.env')

weather_token = os.getenv("WEATHER_TOKEN_KEY")
wxpusher_token = os.getenv("WEATHER_PUSHER_TOKEN")

if weather_token == "d1a6c7c4cac3472eaeda5710efc80ca2":
    print("YES")

print(weather_token, wxpusher_token)
