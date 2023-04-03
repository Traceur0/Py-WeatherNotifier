import json

    

def read_json(path, keyword) -> str:
  """
  @params:
    path    :str - json 파일의 경로
    keyword :str - json 파일에서 검색할 value의 key값에 해당하는 문자열
  """
  
  with open(path, "r") as file:
    json_parse = json.load(file)
    return json_parse[keyword]