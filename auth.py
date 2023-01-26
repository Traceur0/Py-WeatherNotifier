import json
import requests
from time import strftime

from value import API_KEY, AUTH_code, REDIRECT_URI, auth_code_URL, OAUTH_URL



# 인가 코드 발급 : authorization_code
# 수정 예정
def request_auth_code():
    print(auth_code_URL)
    print("\n")
    request = requests.get(auth_code_URL)
    try:
        auth_url = request.url # Redirected URL
        print(auth_url)
    except:
        print("Error!! agreement needed") # 수정 예정
    


# 토큰 발급 : access, refresh 토큰을 발급
'''
    용례
    - 최초 토큰 발급
    - refresh token 만료
'''
def issue_access_token() -> str:
    # 변수 Initialize - UnboundLocalError improvisation
    access_token: str = "N/A"
    refresh_token: str = "N/A"

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
    t = strftime('%Y%m%d%H%M%S')
    with open(f"./response/log/{t}_token_log.json", "w") as log:
        json.dump(request_json, log, indent="\t")

    return access_token


def access_token_info(access_token: str) -> None:
    headers = {
    'Authorization' : "Bearer " + access_token
    }
    token_info = requests.post("https://kapi.kakao.com/v1/user/access_token_info", headers=headers)
    print(token_info.content)


def renew_refresh_token() -> None:
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
    except KeyError: # refresh token 만료 또는 다른 에러
        print("Notice:: Refresh Token expired. Need to issue new Token.")
        issue_access_token()