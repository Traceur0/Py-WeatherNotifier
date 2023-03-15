import json
import requests
from time import strftime

from err import *
from value import API_KEY, AUTH_code, REDIRECT_URI, auth_code_URI, OAUTH_URI, INQUIRY_ACCESS_TOKEN_URI



# 인가 코드(authorization_code) 발급
## 카카오 계정 로그인 과정이 포함되어 있어 개발에 어려움이 있음. 현재 보류중
def request_auth_code() -> None:
    # 요청 URL 확인용
    print(auth_code_URI + "\n")
    request = requests.get(auth_code_URI)
    """
        인가코드 요청 과정
        1. auth_code_URL로 GET요청
        2. 카카오 계정 로그인 페이지로 리다이렉트(세션에 로그인 기록이 있으면 생략)
        3. 이용에 필요한 정보 동의에 동의
        4. 페이지 이동 후 URL의 'code=' 뒷부분이 인가코드로 주어진다
    """
    try:
        auth_url = request.url # Redirected URL
        print(auth_url)
    except:
        ### 수정 예정 - 정보에 동의하지 않는 경우 이외에도 더 많은 예외에 대응 필요
        print("Error!! agreement needed") 
        


# Access, Refresh 토큰 발급
'''
    용례
    - 토큰 '최초' 발급시 
    - refresh token 만료시
'''
def issue_access_token() -> str:
    # 변수 Initialize - improvisation for UnboundLocalError
    access_token: str = "N/A" # not applicable, 해당 없음, 유효하지 않음, 공백
    refresh_token: str = "N/A"

    data = {
        "grant_type" : "authorization_code",
        "client_id" : API_KEY,
        "redirect_URI" : REDIRECT_URI,
        "code" : AUTH_code,
    }

    request = requests.post(OAUTH_URI, data=data)
    try:
        access_token = request.content["access_token"]
        try:
            refresh_token = request.content["refresh_token"]
            
            # 발급받은 Refresh token을 token_response.json에 저장
            with open("./key/token.json", "w") as token_json:
                # json.dump(request, token_json, indent="\t")
                if refresh_token == token_json["refresh_token"]:
                    raise RefreshTokenNotExpired
                else:    
                    token_json["refresh_token"] = refresh_token
        except:
            raise RefreshTokenNotFound
    except:
        raise AccessTokenNotFound

    request_json = request.json()
    time_info = strftime('%Y%m%d%H%M%S')
    with open(f"./response/log/{time_info}_token_log.json", "w") as log:
        json.dump(request_json, log, indent="\t")

    return access_token


def access_token_info(access_token: str) -> None:
    headers = {
    'Authorization' : "Bearer " + access_token
    }
    token_info = requests.post(INQUIRY_ACCESS_TOKEN_URI, headers=headers)
    print(token_info.content)


def renew_refresh_token() -> None:
    with open("./key/token.json", "r") as token_json:
        refresh_token = token_json["refresh_token"]
    data = {
        "grant_type" : "refresh_token",
        "client_id" : API_KEY,
        "refresh_token" : refresh_token,
    }
    request = requests.post(OAUTH_URI, data=data)
    try: 
        refresh_token = request.content["refresh_token"]
    except KeyError: # refresh token 만료 또는 다른 에러
        issue_access_token()
        raise RefreshTokenExpired           ### 확인 필요