import json


def j_read(path: str, keyword: str) -> str:
    """
    @params:
      path    :str - json 파일의 경로
      keyword :str - json 파일에서 검색할 value의 key값에 해당하는 문자열
    """

    with open(path, "r") as file:
        json_parse = json.load(file)
        return json_parse[keyword]


def j_write(path: str, keyword: str, value: str) -> None:
    """
    @params:
      path    :str - json 파일 경로
      keyword :str - 파일에서 찾을 value의 key값에 해당하는 문자열
      value   :str - 수정할 내용의 문자열
    """

    with open(path, "r") as file:
        json_parse = json.load(file)
        json_parse[keyword] = value

    with open(path, "w", encoding="utf-8") as file:
        json.dump(json_parse, file, indent="\t")
