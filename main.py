# from auth import request_auth_code, issue_access_token, renew_refresh_token, access_token_info
# from send_msg import send_message

from auth import issue_token, request_auth_code
from send_msg import send_message
import json



with open("./plaintext/token.json", "r") as token_file:
  token_json = json.load(token_file)
A_token = token_json["access_token"]

send_message(A_token)

# A_token = issue_access_token()
# request_auth_code()