# Description

## 프로젝트 파일 구조

> ├─ log  
> │ ├─  
> │ ├─  
> │ └─  
> ├─ plaintext  
> │ ├─ json  
> │ ├─  
> │ └─  
> ├─ .gitignore  
> ├─ auth.py  
> ├─ description.md  
> ├─ err.py  
> ├─ init.py  
> ├─ io_func.py  
> ├─ main.py  
> ├─ README.md  
> ├─ send_msg.py  
> ├─ value.py  
> └─ weather_info.py

### I/O (JSON 파일 읽기/쓰기 관련 문제)

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

### 원인불명 - 메세지 전송시 이미지가 나타나지 않음

- 이미지 URL은 정상적으로 주어졌음
- 메세지 전송 요청 과정에서 문제가 있는것으로 추정됨(이미지에 대한 제한사항에 맞지 않는 이미지를 사용하는 등의 문제)
- 이미지 제한 사항
  > RFC2396, RFC1034, RFC1123을 준수해야 함
  > 200x200픽셀 이상, 2MB 이하

### 웹 링크가 정상적으로 동작하지 않음

- 내 애플리케이션 > 앱 설정 > 플랫폼 페이지에서 사이트 도메인을 등록, 메세지 전송 부분에 이동할 URL과 함께 요청했음에도 도착 메세지에 상호작용시 요청한 페이지가 아닌 플렛폼 수정 페이지의 기본 도메인으로 연결됨
