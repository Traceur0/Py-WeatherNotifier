import json
import webbrowser
from time import strftime

import requests

from err import RefreshTokenStillValid
from io_func import j_read, j_write
from value import (API_KEY, INQUIRY_ACCESS_TOKEN_URI, OAUTH_URI, REDIRECT_URI,
                   AUTH_code, auth_code_URI, PATH_TOKEN)


PATH_TEST = "./test.json"

# 인가 코드(authorization_code) 발급


def request_auth_code() -> None:
    # 요청 URL 확인용
    print(auth_code_URI + "\n")
    # request = requests.get(auth_code_URI)
    webbrowser.open(auth_code_URI, new=1, autoraise=True)
    while True:
        access_token_input = input("AccessTokenValue: ")
        if access_token_input == "" or None:
            print("Input value vacant. retry")
        elif access_token_input != "" or None:
            print(access_token_input)
            break
    j_write(PATH_TEST, "authorization_code", access_token_input)
    j_read(PATH_TEST, "authorization_code")

    """
        인가코드 요청 과정
        1. auth_code_URL로 GET요청
        2. 카카오 계정 로그인 페이지로 리다이렉트(세션에 로그인 기록이 있으면 생략)
        3. 이용에 필요한 정보 동의에 동의
        4. 페이지 이동 후 URL의 'code=' 뒷부분이 인가코드로 주어진다
    """
    '''
    try:
        auth_url = request.url # Redirected URL
        print(auth_url)
    except:
        ### 수정 예정 - 정보에 동의하지 않는 경우 이외에도 더 많은 예외에 대응 필요
        print("Error!! agreement needed")
    '''


'''
    용례
    - 토큰 '최초' 발급 시 
    - refresh token 만료 시

    * 토큰 발급 시에는 항상 access, refresh token이 함께 발급
'''


def issue_token() -> None:    # 변수 Initialize - improvisation for UnboundLocalError
    access_token: str = "N/A"  # not applicable, 해당 없음, 유효하지 않음, 공백
    refresh_token: str = "N/A"

    data = {
        "grant_type": "authorization_code",
        "client_id": API_KEY,
        "redirect_URI": REDIRECT_URI,
        "code": AUTH_code,
    }

    request = requests.post(OAUTH_URI, data=data)
    content = request.json()

    try:
        print(content)      # DEBUGGING
        access_token = content["access_token"]
        refresh_token = content["refresh_token"]
    except:
        # 발급 과정에서 에러 발생
        print(content)
        raise RefreshTokenStillValid
    else:
        # I/O
        with open(PATH_TOKEN, "r") as token_json:
            if token_json["refresh_token"] != "":
                ...
            # renew_both_token()
            else:
                with open(PATH_TOKEN, "w") as token_json:
                    token_json["refresh_token"] = refresh_token
                    token_json["access_token"] = access_token
            '''
                #LOGGING

                # json.dump(request, token_json, indent="\t")
                if refresh_token == token_json["refresh_token"]:
                    raise #RefreshTokenNotExpired
                else:       # 발급받은 Refresh token을 token_response.json에 저장
            '''

    # Logging
    request_json = request.json()
    time_info = strftime('%Y%m%d%H%M%S')
    # I/O
    with open(f"./response/log/{time_info}_token_log.json", "w") as log:
        json.dump(request_json, log, indent="\t")


def access_token_info(access_token: str) -> None:
    headers = {
        'Authorization': "Bearer " + access_token
    }
    token_info = requests.get(INQUIRY_ACCESS_TOKEN_URI, headers=headers)
    print(token_info.content)


# 기존의 refresh 토큰을 이용하여 Access token 재발행과 동시에 refresh token도 재발행
def renew_both_token(refresh_token: str) -> None:
    '''
        with open("./key/token.json", "r") as token_json:
        refresh_token = token_json["refresh_token"]
    '''
    data = {
        "grant_type": "refresh_token",
        "client_id": API_KEY,
        "refresh_token": refresh_token,
    }
    request = requests.post(OAUTH_URI, data=data)
    content = request.json()
    try:
        # response.json에 refresh token값이 있는지 확인
        refresh_token = content["refresh_token"]
    except KeyError:
        # refresh token값이 갱신되지 않았다면 유효기간이 1개월 미만으로 남은 경우
        # issue_token()
        raise RefreshTokenStillValid
    else:
        # I/O
        with open("./plaintext/token.json", "w") as token_json:
            token_json["refresh_token"] = refresh_token
