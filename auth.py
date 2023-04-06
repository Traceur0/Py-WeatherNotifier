import json
import webbrowser
from time import strftime

import requests

from err import RefreshTokenStillValid
from io_func import j_read, j_write, Write
from value import (API_KEY, INQUIRY_ACCESS_TOKEN_URI, OAUTH_URI, REDIRECT_URI,
                   AUTH_code, auth_code_URI, PATH_TOKEN)


def request_auth_code() -> None:
    """
    인가 코드(authorization_code) 발급, 저장 함수
    @params, return:
        None
    """

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

    # TEST CODE
    PATH_TEST: str = "./plaintext/test.json"
    j_write(PATH_TEST, "authorization_code", access_token_input)
    j_read(PATH_TEST, "authorization_code")

    '''
    j_write(PATH_TOKEN, "authorization_code", access_token_input)
    j_read(PATH_TOKEN, "authorization_code")
    '''
    print("All DONE!")


def issue_token(authorization_code: str) -> None:
    """
    - 토큰 '최초' 발급 시
    - refresh token 만료 시
    * (토큰 발급 시에는 항상 access, refresh token이 함께 발급)

    @params
        authorization_code  : str - 인가코드값 
    return:
        None
    """

    access_token: str = "N/A"  # not applicable, 해당 없음, 유효하지 않음, 공백
    refresh_token: str = "N/A"

    data = {
        "grant_type": "authorization_code",
        "client_id": API_KEY,
        "redirect_URI": REDIRECT_URI,
        "code": authorization_code,
    }

    request = requests.post(OAUTH_URI, data=data)
    content = request.json()

    try:
        response = f"""
  token type                : {content["token_type"]}
  access token              : {content["access_token"]}
  expires in                : {content["expires_in"]}
  refresh token             : {content["refresh_token"]}
  refresh token expires in  : {content["refresh_token_expires_in"]}
    """
        access_token = content["access_token"]
        refresh_token = content["refresh_token"]
    except KeyError:
        print(content)
        # 발급 과정에서 에러 발생
        raise Exception  # RefreshTokenStillValid ?
    else:
        print(response)
        # I/O - 토큰값 JSON 파일에 저장 - 수정 필요
        PATH = Write(PATH_TOKEN)
        PATH.j_writes("refresh_token", refresh_token)
        PATH.j_writes("access_token", access_token)
    print("End Of Line")
    """
    # Logging
    request_json = request.json()
    time_info = strftime('%Y%m%d%H%M%S')
    # I/O
    with open(f"./response/log/{time_info}_token_log.json", "w") as log:
        json.dump(request_json, log, indent="\t")
        '''
        if refresh_token == token_json["refresh_token"]:
            raise  # RefreshTokenNotExpired
        else:       # 발급받은 Refresh token을 token_response.json에 저장
        '''
    """


def access_token_info(access_token: str) -> None:
    """
    엑세스 토큰의 유효기간 등 토큰 관련 정보를 조회
    @params:
        access_token    : str - 액세스 토큰값
    @return:
        None
    """
    headers = {
        'Authorization': "Bearer " + access_token
    }
    token_info = requests.get(INQUIRY_ACCESS_TOKEN_URI, headers=headers)
    print(token_info.content)


def renew_both_token(refresh_token: str) -> None:
    """
    기존의 refresh 토큰을 이용하여 Access token, refresh token 모두 재발행
    @params:
        refresh_token   : str - 리프레시 토큰값
    @return:
        None
    """

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
