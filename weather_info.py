from bs4 import BeautifulSoup
import json
import requests



# 기본 변수
nav_search_URL = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=1&acq=오늘+서울+날씨&qdt=0&ie=utf8&query=오늘+서울+날씨"
city_name = "seoul"
lang_code = "kr"


# Naver "오늘 서울 날씨" searchedWeatherInfo
basic_info = requests.get(nav_search_URL)
parsing = BeautifulSoup(basic_info.text ,"html.parser")
naver_wthr_info = parsing.select_one("div.temperature_text").text


# OpenWeather api weatherInfo
with open("./plaintext/key.json", "r") as key_file:
    key_json = json.load(key_file)
key_O = key_json["openWeather"]["openWeather_key"]
open_wthr_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key_O}&lang={lang_code}&units=metric"

open_wthr = requests.get(open_wthr_URL).text
OW_json = json.loads(open_wthr)
OW_dic_main = OW_json["main"]
# OW_dic_wthr = OW_json["weather"][0]
# 기온_일반 = str(OW_json["main"]["temp"])
# 기온_체감 = str(OW_json["main"]["feels_like"])
# 기온_최저 = str(OW_json["main"]["temp_min"])
# 기온_최대 = str(OW_json["main"]["temp_max"])
open_wthr_info = str(OW_json["main"]["temp"]) + "°"