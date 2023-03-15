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


# 인가코드 요청 - 로그인
## Http Response Code 리다이렉트
REDIRECT_URI = "https://example.com/oauth"


# 토큰 발급을 위한 인가 코드 받기 
## *API_KEY만 다른 모듈에서 Import
auth_code_URI = f"https://kauth.kakao.com/oauth/authorize?&response_type=code&client_id={API_KEY}&redirect_uri={REDIRECT_URI}"


# 액세스 토큰 요청/갱신
OAUTH_URI = "https://kauth.kakao.com/oauth/token" 


# 메세지 전송 요청
SEND_MSG_URI = "https://kapi.kakao.com/v2/api/talk/memo/default/send"


# 액세스 토큰 정보 조회 .
INQUIRY_ACCESS_TOKEN_URI = "https://kapi.kakao.com/v1/user/access_token_info"



## Refresh token 과 Access token
## Refresh token은 Access token과 비교해서 상대적으로 긴 유효기간을 가지고 있음.