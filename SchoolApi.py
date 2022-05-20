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
        # print(response.text)

        try:
            j_response = json.loads(response.text)[self.sub_url]
            if j_response[0]["head"][0]["list_total_count"] == 1:
                return j_response[1]["row"][0]
            else:
                return j_response[1]["row"]
        except:
            print("주인님이 말하시는 데이터가 없어요....")
            return response.text

    def get_school_info(self):
        data = self.get_data()
        try:
            SchoolApi.schoolinfo = {
            "ATPT_OFCDC_SC_CODE": data["ATPT_OFCDC_SC_CODE"],
            "SD_SCHUL_CODE": data["SD_SCHUL_CODE"]
            }
        except:
            print("도비가 학교를 못 찾겠어요 :(\n좀 더 정확하게 입력해주세요")
            print("도비는 주인님이 말한 걸 못 찾으면 슬퍼요.. 아무고토 못해요...")
            quit()

    def meal(self):
        data = self.get_data()
        try:
            string = data["DDISH_NM"].replace("<br/>", "\n")
            characters = "1234567890."
            for x in range(len(characters)):
                string = string.replace(characters[x],"")
            return string
        except:
            return "오늘은 급식이 없는 날입니다, 주인님!"

    def time(self):
        data = self.get_data()
        string = ""
        try:
            for i in data:
                string += i["ITRT_CNTNT"] + "\n"
            return string
        except:
            return "오늘은 시간표가 없는 날이에요...!"

    def schedule(self):
        data = self.get_data()
        try:
            return data["EVENT_NM"]+"이(가) 있습니다."
        except:
            return "오늘은 주인님의 일정이 아무 것도 없어요!"