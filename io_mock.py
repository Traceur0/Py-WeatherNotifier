import json



class IO_Func:
    def __init__(self, path):
        self.path = path


    def read(self, keyword: str) -> str:
        with open(self.path, "r") as file:
            json_parse = json.load(file)
            foo =  json_parse[keyword]
      

    def write(self, keyword: str, value: str) -> None:
        with open(self.path, "r") as file:
            json_parse = json.load(file)
            # 데이터 수정
            json_parse[keyword] = value

        # 기존 파일 덮어쓰기
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(json_parse, file, indent="\t")


class IO(IO_Func):
    def __init__(self, path):
        self.path = path
        
    def _with(self, **kargs):
        file = open(self.path, "r")
        wrapper()
        file.close()

        # wrapper 부분에 read() 또는 write()를 파리미터로 넣을 수 있도록 코딩
