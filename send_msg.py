import requests

from weather_info import OW_WEATHER_INFO, NAVER_WEATHER_INFO
from value import SEND_MSG_URI



def send_message(access_token: str):
    headers = {
    'Authorization' : "Bearer" + " " + access_token
    }
    # KakaoTalk Rest API parameter
    data = { "template_object" : {
            "object_type": "list",
            "header_title": "오늘 서울 기온",
            "header_link": {
                "web_url": "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=오늘 서울 날씨",
                "mobile_web_url": "https://m.search.naver.com/search.naver?sm=mtp_sly.hst&where=m&query=오늘 서울 날씨&acr=2",
                "android_execution_params": "main",
            },
            "contents": [{
                    "title": OW_WEATHER_INFO,
                    "description": "OpenWeather API",
                    "image_url": "https://api.dicebear.com/5.x/icons/svg?icon=thermometer",
                    "image_width": "640",
                    "image_height": "640",
                    "link": {
                        "web_url": "https://openweathermap.org/",
                        "mobile_url": "https://openweathermap.org/",
                        "android_execution_params": "/",
                    }
                },
                {
                    "title": NAVER_WEATHER_INFO,
                    "description": "Naver",
                    "image_url": "https://api.dicebear.com/5.x/icons/svg?icon=thermometer",
                    "image_width": "640",
                    "image_height": "640",
                    "link": {
                        "web_url": "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=오늘 은평구 날씨",
                        "mobile_url": "https://m.search.naver.com/search.naver?sm=mtp_sly.hst&where=m&query=오늘 은평구 날씨&acr=2",
                        "android_execution_params": "/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=오늘 은평구 날씨",
                    }
                }
            ]
        }
    }

    # URL로 POST 요청
    msg_rqst = requests.post(SEND_MSG_URI, headers=headers, data=data)
    return print(msg_rqst.content, access_token)