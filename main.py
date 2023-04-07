from auth import issue_token, request_auth_code
from io_func import j_read
from send_msg import send_message
from value import PATH_TEST


request_auth_code()

issue_token(j_read(PATH_TEST, "authorization_code"))

send_message(j_read(PATH_TEST, "access_token"))
