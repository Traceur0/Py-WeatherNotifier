# from auth import request_auth_code, issue_access_token, renew_refresh_token, access_token_info
# from send_msg import send_message

from auth import issue_token, request_auth_code
# from io_class import JSON_Read, JSON_Write
from io_func import j_read
# from send_msg import send_message
# from value import PATH_KEY, PATH_TOKEN
# import json


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
# A_token = issue_access_token()
# request_auth_code()
request_auth_code()
