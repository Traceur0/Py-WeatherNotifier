import json



def read_json(
    keyword_search: str
    ):
  """
  @params:
    path    :str - 
    keyword :str - json 파일에서 검색할 value의 key의 문자열
  """
  with open("./plaintext/token.json", "r") as token_file:
    json_parse = json.load(token_file)
    return json_parse[keyword_search]