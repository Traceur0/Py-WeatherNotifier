from auth import issue_token, request_auth_code
from io_func import j_read
# from send_msg import send_message


# json_str = JSON_Read("./test.json","test").read_json()
'''
json_str = read_json("./test.json", "test")
print(json_str)
'''

''' TEST CODE
with open("./plaintext/token.json", "r") as file:
  token_json = json.load(file)
A_token = token_json["access_token"]

send_message(A_token)
'''

request_auth_code()

issue_token(j_read("./plaintext/test.json", "authorization_code"))
