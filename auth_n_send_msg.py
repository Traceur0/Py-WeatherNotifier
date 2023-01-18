import requests
import json

from weather_info import open_wthr_info, naver_wthr_info
from url import REDIRECT_URI, renew_URL, OAUTH_URL, SEND_MSG_URL




with open("./plaintext/key.json", "r") as key_file:
    key_json = json.load(key_file)
REQUEST_KEY = key_json["kakaoTalk"]["kakao_api_key"]
AUTH_code = key_json["kakaoTalk"]["authorization_code"]
RF_token = key_json["kakaoTalk"]["refresh_token"]


def issue_refresh_token(): 
    data = {
        "grant_type" : "refresh_token",
        "client_id" : REQUEST_KEY,
        "redirect_URI" : REDIRECT_URI,
        "code" : AUTH_code,
        "refresh_token" : RF_token,
    }

    ###  ERROR  ###
    oauth_request_POST = requests.post(OAUTH_URL, data=data)
    token = oauth_request_POST.json()

    with open("./plaintext/token_response.json", "w") as token_json:
        json.dump(token, token_json, indent="\t")
    with open("./plaintext/token_response.json", "r") as token_json:
        token_data = json.load(token_json)
    
    # save issued value : refresh_token in key.json
    try: 
        refresh = token_data["refresh_token"]
    except KeyError: # if error occured
        print("NOTICE : lastest refresh token is still valid.")
    else: # if error not occured
        with open("./plaintext/key.json", "r") as code_json:
            key_f_token_json = json.load(code_json)
        key_f_token_json["kakaoTalk"]["refresh_token"] = refresh ### ?

    # *무슨 절차인지 기술할 것*
    try:
        result = token_data["access_token"] # return
    except KeyError:
        renew_request_POST = requests.post(renew_URL, data=data)
        renew = renew_request_POST.json()

        with open("./plaintext/token_response.json", "w") as renew_json:
            json.dump(renew, renew_json, indent="\t")
        issue_refresh_token()
    return result
    ###  ERROR  ###


access_token = issue_refresh_token()

# access_token값 배정하기
headers = {
    'Authorization' : "Bearer " + access_token
}


def renew_token():
    data = {
        
    }


def send_message():
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