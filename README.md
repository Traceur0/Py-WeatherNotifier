# Py-DailyWeatherNotifier

## <u>본 코드는 미완성 코드입니다</u>

> api와 날씨 웹사이트를 통해 기온정보를 모으고 카카오톡을 통해 전송합니다.

---

### 이전 개발 중단 22.05.17

---

### 개발 재시작 23.01.12

---

> 한계
>
> - OAuth 2.0 특성상 수동 로그인을 요구하고 완전한 자동화가 불가능하다고 생각된다
>
> - ~~셀레니움으로 Authorization_code(인가 코드)를 발급받는 부분을 자동화하는 방법이 있으나 사용자 ID, Password 입력이 필요하다~~
> - ~~Kakao API 업데이트 이후 셀레니움을 이용한 방법도 사용 불가~~
>
> - 웹서버가 필요
>
> - 그러나 Flutter를 이용해 모바일 앱으로 제작한다면 위에 서술한 부분을 무시하고 구현 가능

---

> 특이사항
>
> - REST Api의 headers 부분에 사소한 버그가 있다
>
> ```python
> headers = {
>    'Authorization' : "Bearer " + access_token
>    }
> ```
>
> 위 코드처럼 문자열 "Bearer" 와 엑세스 토큰 사이에 공백이 한칸 있어야 정상적으로 요청이 가능하다
>
> - ex) Bearer 2are34ldafef...
> -          ^^^
