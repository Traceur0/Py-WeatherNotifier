from kakao_login import issue_refresh_token, send_message



access_token = issue_refresh_token()
send_message(access_token)