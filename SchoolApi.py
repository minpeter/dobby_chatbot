import requests
import json
import filemanager as fm

class SchoolApi:

    params = {
        "KEY": fm.read_api_key("neis"),
        "Type": "json",
    }

    schoolinfo = {}

    base_url = "https://open.neis.go.kr/hub/"

    def __init__(self, sub_url, params):
        self.sub_url = sub_url
        self.params = params

    def get_data(self):
        URL = SchoolApi.base_url + self.sub_url
        self.params.update(SchoolApi.params)
        self.params.update(SchoolApi.schoolinfo)
        response = requests.get(URL, params=self.params)

        # print(response.text)    #for debug
        try:
            return json.loads(response.text)[self.sub_url][1]["row"][0]
        except:
            print("해당하는 데이터가 존재하지 않습니다.")
            return json.loads(response.text)

    def get_school_info(self):
        data = self.get_data()
        try:
            SchoolApi.schoolinfo = {
            "ATPT_OFCDC_SC_CODE": data["ATPT_OFCDC_SC_CODE"],
            "SD_SCHUL_CODE": data["SD_SCHUL_CODE"]
            }
        except:
            print("도비가 학교를 못 찾겠어요 :(\n좀 더 정확하게 입력해주세요")

    def meal(self):
        data = self.get_data()
        try:
            return data["DDISH_NM"].replace("<br/>", "\n")
        except:
            return "오늘은 급식이 없습니다."

    def time(self):
        data = self.get_data()
        try:
            return data["TIME"]
        except:
            return "오늘은 시간표가 없습니다."

    def schedule(self):
        data = self.get_data()
        try:
            return data["EVENT_NM"]+"이(가) 있습니다."
        except:
            return "오늘은 일정이 없습니다."
