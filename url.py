### This file is made for URL-compliation purpose.



## 인가코드 요청
# 리다이렉트
# Http Response Code 리다이렉트
REDIRECT_URI = "https://example.com/oauth"

## 만료된 Fresh Token 재발행 요청URL
# 또는 토큰 발급을 위한 인가코드 받기 
# *REQUEST_KEY의 경우에만 외부 파일에서 값을 받아옴*
renew_URL = f"https://kauth.kakao.com/oauth/authorize?client_id={REQUEST_KEY}&redirect_uri={REDIRECT_URI}&response_type=code"


## 토큰 요청/갱신
# 토큰 요청/갱신
OAUTH_URL = "https://kauth.kakao.com/oauth/token" 


## 메세지 전송 요청
# 메세지 전송 요청 API URL
SEND_MSG_URL = "https://kapi.kakao.com/v2/api/talk/memo/default/send"


# Refresh token 과 Access token