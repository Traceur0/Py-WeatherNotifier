import json

import requests
from bs4 import BeautifulSoup



# Naver "오늘 서울 날씨" searchedWeatherInfo
nav_search_URL : str = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=1&acq=오늘+서울+날씨&qdt=0&ie=utf8&query=오늘+서울+날씨"

basic_info = requests.get(nav_search_URL)
parsing = BeautifulSoup(basic_info.text ,"html.parser")
NAVER_WEATHER_INFO = parsing.select_one("div.temperature_text").text


# OpenWeather api weatherInfo
with open("./plaintext/key.json", "r") as file:     
    key = json.load(file)    

city_name : str = "seoul"
key_OW = key["openWeather_api_key"]
lang_code : str = "kr"

open_wthr_URL : str = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key_OW}&lang={lang_code}&units=metric"

open_wthr = requests.get(open_wthr_URL).text
OW_json = json.loads(open_wthr)
OW_dic_main = OW_json["main"]
"""
    OW_dic_wthr = OW_json["weather"][0]
    기온_일반 = str(OW_json["main"]["temp"])
    기온_체감 = str(OW_json["main"]["feels_like"])
    기온_최저 = str(OW_json["main"]["temp_min"])
    기온_최대 = str(OW_json["main"]["temp_max"])
"""
OW_WEATHER_INFO = str(OW_json["main"]["temp"]) + "°"