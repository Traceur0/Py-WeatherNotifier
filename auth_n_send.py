import json
import requests
from time import strftime

from weather_info import open_wthr_info, naver_wthr_info
from value import *



t = strftime('%Y%m%d%H%M%S')

# 토큰 발급 : access, refresh 토큰을 발급
## 최초로 토큰을 발급받거나 refresh 토큰이 만료된 경우 실행
def issue_access_token():
    access_token = ""
    refresh_token = ""
    data = {
        "grant_type" : "authorization_code",
        "client_id" : API_KEY,
        "redirect_URI" : REDIRECT_URI,
        "code" : AUTH_code,
    }

    request = requests.post(OAUTH_URL, data=data)
    try:
        access_token = request.content["access_token"]
        try:
            refresh_token = request.content["refresh_token"]
            
            # 발급받은 Refresh token을 token_response.json에 저장
            with open("./key/token.json", "w") as token_json:
                # json.dump(request, token_json, indent="\t")
                if refresh_token == token_json["refresh_token"]:
                    print("Notice:: Refresh Token is still valid.")
                    print("system will maintain existed Refresh Token.")
                else:    
                    token_json["refresh_token"] = refresh_token
        except:
            print("Could not find 'refresh_token'.")
    except:
        print("Could not find 'access_token'.")

    request_json = request.json()
    with open(f"./response/log/{t}_token_log.json", "w") as log:
        json.dump(request_json, log, indent="\t")

    return access_token


def access_token_info(access_token):
    headers = {
    'Authorization' : "Bearer " + access_token
    }
    token_info = requests.post("https://kapi.kakao.com/v1/user/access_token_info", headers=headers)
    print(token_info.content)


def renew_refresh_token():
    with open("./key/token.json", "r") as token_json:
        refresh_token = token_json["refresh_token"]
    data = {
        "grant_type" : "refresh_token",
        "client_id" : API_KEY,
        "refresh_token" : refresh_token,
    }
    request = requests.post(OAUTH_URL, data=data)

    try: 
        refresh_token = request.content["refresh_token"]
    except KeyError: # refresh token 만료 || 다른 에러
        print("Notice:: Refresh Token expired. Need to issue new Token.")
        issue_access_token()

def send_message(access_token):
    headers = {
    'Authorization' : "Bearer " + access_token
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
                    "title": open_wthr_info,
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
                    "title": naver_wthr_info,
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
    msg_rqst = requests.post(SEND_MSG_URL, headers=headers, data=data)
    return print(msg_rqst.content, access_token)