"""
  DEPRECATED
"""

import json



class JSON_Read:
  """
    @params:
      path    :str - json 파일의 경로
      keyword :str - json 파일에서 검색할 value의 key값에 해당하는 문자열
  """

  @staticmethod
  def read_json_2(path : str, keyword: str) -> str:
    with open(path, "r") as file:
      json_parse = json.load(file)
      return json_parse[keyword]


  def __init__(self, path : str, keyword : str):
    self.path = path
    self.keyword = keyword


  def read_json(self) -> str:
    with open(self.path, "r") as file:
      json_parse = json.load(file)
      return json_parse[self.keyword]


class JSON_Write:
  """
    @params:
      path    :str - json 파일 경로
      keyword :str - 파일에서 찾을 value의 key값에 해당하는 문자열
      value   :str - 수정할 내용의 문자열
  """
  
  def __init__(self, path : str, keyword : str, value : str):
    self.path = path
    self.keyword = keyword
    self.value = value


  @classmethod
  def write_json(cls) -> None:
    with open(cls.path, "r") as file:
      json_parse = json.load(file)

    json_parse[cls.keyword] = cls.value
    
    with open(cls.path, "w", encoding="utf-8") as file:
      json.dump(json_parse, file, indent="\t")