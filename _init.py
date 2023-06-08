from auth import issue_token



def initialize():
  # main.py에서 실행 시
  if __name__ == "__main__":
    issue_token()