import requests
import json


from weather_info import open_wthr_info, naver_wthr_info



oauth_url = "https://kauth.kakao.com/oauth/token"

with open("./plaintext/key.json", "r") as key_file:
    key_json = json.load(key_file)
key_K = key_json["kakaoTalk"]["kakao_key"]
authorization_code = key_json["kakaoTalk"]["authorization_code"]
# REFRESH TOKEN
rf_token = key_json["kakaoTalk"]["refresh_token"]

REDIRECT_URI = "https://example.com/oauth"

# 토큰 재발행을 위한 코드를 발급하는 URL
reissuance_url = f"https://kauth.kakao.com/oauth/authorize?client_id={key_K}&redirect_uri={REDIRECT_URI}&response_type=code"

def Issue_refresh_token(): 
    data = {
        "grant_type" : "refresh_token",
        "client_id" : key_K,
        "redirect_URI" : REDIRECT_URI,
        "code" : authorization_code,
        "refresh_token" : rf_token,
    }

    # request URL / data : additional requestInfo(parameter) ==> 이 부분을 함수로 만들지 말고, 58번 행에는 변수명을 다르게 하여 작성해보자
    def request_POST(url, param):
        request_POST = requests.post(url, data=param)
        token = request_POST.json()

        # save responseInfo in .json (allocating to variable)
        with open("./plaintext/k_token.json", "w") as token_json:
            json.dump(token, token_json, indent="\t")


    request_POST(oauth_url, data)
    with open("./plaintext/k_token.json", "r") as token_json:
        token_read = json.load(token_json)
    # save issued value : refresh_token in key.json
    try: 
        refresh = token_read["refresh_token"]
    except KeyError: # if error occured
        print("NOTICE : lastest refresh token is still valid.")
    else: # if error not occured
        with open("./plaintext/key.json", "r") as code_json:
            key_f_token_json = json.load(code_json)
        key_f_token_json["kakaoTalk"]["refresh_token"] = refresh

    try:
        result = token_read["access_token"]
    except KeyError:
        request_POST(reissuance_url, data)
        Issue_refresh_token()
    return result


def Send_message(access_token):
    msg_sending_URL = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    headers = {
        'Authorization' : "Bearer " + access_token
    }

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

    msg_rqst = requests.post(msg_sending_URL, headers=headers, data=data)
    return print(msg_rqst.content, access_token)


'''
data = { "template_object" : {
        "object_type" : "text",
        "text" : "weatherForecast",
        "link" : {
            "web_url" : "https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query=오늘+서울+날씨"
        }
    }
}
'''