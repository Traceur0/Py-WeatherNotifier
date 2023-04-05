<!-- -*- coding: utf-8 -*- -->

# Py-WeatherNotifier

> <u>본 코드는 미완성 코드입니다</u>

- api와 날씨 웹사이트를 통해 기온정보를 모으고 카카오톡을 통해 전송합니다.

---

## 프로그램 동작 순서

> 카카오 계정을 통한 인증 REST API 이용 안내를 따라 작성한 코드입니다
> https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api#before-you-begin-process

1. 카카오계정 로그인 후 리다이렉트 페이지로 이동 후 REDIRECT URI을 통해 Authorization_code 수령

2. Authorization_code로 fresh_token 수령

   > authorization_code의 경우

3. fresh_token으로 access_token 수령

   > fresh_token이 만료(1달간 유효)된 경우 2번으로 돌아가 fresh_token을 수령하는 과정 필요

4. OpenWeatherAPI, Web Crawler등을 통해 날씨 정보 수집

5. access_token을 사용하여 수집한 정보를 카카오톡 메세지 형태로 전송(자신에게 전송)

---

## 이후 개발 계획

- OAuth 2.0 특성상 수동 로그인을 요구하여 그 과정에서 유저 인풋 필수

- api 요청과 같은 부분은 코드를 작성하여 자동화하고 로그인 부분만 수동으로 할 수 있도록 하는 방법을 탐색중에 있음
  (로그인을 자동화할 수 있는 방법이 있으나 보안취약점 발생, 로그인 서버에서 봇을 통한 어뷰징 시도로 오인하여 차단당할 수 있는 등의 문제점이 발생한다)
- 이 과정을 Flutter를 이용해 모바일 앱으로 제작 고려중
