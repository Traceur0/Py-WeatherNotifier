json 읽고 쓰기 방식을 코드로 작성하는 데 문제가 있는 것으로 확인됩니다

TypeError: '\_io.TextIOWrapper' object is not subscriptable

- 이 오류를 제거하려면 아래와 같이 Read모드로 읽은 json파일을 json.load로 한번 로드하여 변수에 할당해야만 합니다.

```python
with open("./plaintext/token.json", "r") as token_file:
    token_json = json.load(token_file)
AUTH_code = token_json["authorization_code"]
R_token = token_json["refresh_token"]
```
