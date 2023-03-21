<!-- -*- coding: utf-8 -*- -->

# Py-WeatherNotifier

### <u>본 코드는 미완성 코드입니다</u>

- api와 날씨 웹사이트를 통해 기온정보를 모으고 카카오톡을 통해 전송합니다.

---

## 프로그램 동작 순서

> 카카오 계정을 통한 REST API 인증 과정은 Kakao developers에서 안내하는 과정과 동일
> https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api#before-you-begin-process

1. 카카오계정 로그인 후 리다이렉트 페이지로 이동 후 REDIRECT URI을 통해 Authorization_code 수령
2. Authorization_code로 fresh_token 수령
   > authorization_code의 경우
3. fresh_token으로 access_token 수령
   > fresh_token이 만료(1달간 유효)된 경우 2번으로 돌아가 fresh_token을 수령하는 과정 필요
4. access_token을 사용하여 카카오톡 메세지 전송(자신에게 전송)

---

## 이후 개발 계획

- OAuth 2.0 특성상 수동 로그인을 요구하여 그 과정에서 유저 인풋을 받아야 한다
- ~~셀레니움으로 Authorization_code(인가 코드)를 발급받는 부분을 자동화하는 방법이 있으나 사용자 ID, Password 입력이 필요하다~~
- ~~Kakao API 업데이트 이후 셀레니움을 이용한 방법도 사용 불가~~

- api 요청과 같은
- 이 과정을 Flutter를 이용해 모바일 앱으로 제작 예정
