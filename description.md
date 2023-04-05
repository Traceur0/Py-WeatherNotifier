json 읽고 쓰기 방식을 코드로 작성하는 데 문제가 있는 것으로 확인됩니다

TypeError: '\_io.TextIOWrapper' object is not subscriptable

- 이 오류를 제거하려면 아래와 같이 Read모드로 읽은 json파일을 json.load로 한번 로드하여 변수에 할당해야만 합니다.

```python
with open("./plaintext/token.json", "r") as token_file:
    token_json = json.load(token_file)
AUTH_code = token_json["authorization_code"]
R_token = token_json["refresh_token"]
```

### 인가코드 요청 과정

> 1. auth_code_URL로 GET요청
> 2. 카카오 계정 로그인 페이지로 리다이렉트(세션에 로그인 기록이 있으면 생략)
> 3. 이용에 필요한 정보 동의에 동의
> 4. 페이지 이동 후 URL의 'code=' 뒷부분이 인가코드로 주어진다
