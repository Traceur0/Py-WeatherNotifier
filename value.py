### This file is made for URL-compliation purpose.
import json



# API 요청에 필요한 값들을 json에서 import
with open("./plaintext/key.json", "r") as key_file:
    key_json = json.load(key_file)
API_KEY = key_json["kakaoTalk"]["kakao_api_key"]

with open("./plaintext/token.json", "r") as token_file:
    token_json = json.load(token_file)
AUTH_code = token_json["authorization_code"]
R_token = token_json["refresh_token"]



## 인가코드 요청 - 로그인
# 리다이렉트
# Http Response Code 리다이렉트
REDIRECT_URI = "https://example.com/oauth"


## 또는 토큰 발급을 위한 인가 코드 받기 
# *REQUEST_KEY의 경우에만 외부 파일에서 값을 받아옴*
# * 또한 최초 실행시 parameter를 입력한 해당 주소로 이동하여 KakaoTalk 계정 로그인을 마친 후 이동된 URL의 마지막 부분(... &response_type=)의 숫자가 Autherization_code이다.
auth_code_URL = f"https://kauth.kakao.com/oauth/authorize?&response_type=code&client_id={API_KEY}&redirect_uri={REDIRECT_URI}"


## 토큰 받기
# 토큰 요청/갱신
OAUTH_URL = "https://kauth.kakao.com/oauth/token" 


## 메세지 전송 요청
# 메세지 전송 요청 API URL
SEND_MSG_URL = "https://kapi.kakao.com/v2/api/talk/memo/default/send"


# Refresh token 과 Access token
# 리프레시 토큰은 엑세스 토큰과 비교해서 상대적으로 긴 유효기간을 가지고 있음.