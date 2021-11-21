import requests
import json
from SchoolApi import filemanager as fm

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

        return json.loads(response.text)[self.sub_url][1]["row"][0]

    def get_school_info(self):
        school_info = self.get_data()
        SchoolApi.schoolinfo = {
            "ATPT_OFCDC_SC_CODE": school_info["ATPT_OFCDC_SC_CODE"],
            "SD_SCHUL_CODE": school_info["SD_SCHUL_CODE"]
        }
    
    def meal(self):
        data = self.get_data()
        return data["DDISH_NM"].replace("<br/>", "\n")

    def time(self):
        data = self.get_data()
        return data["TIME"]

    def schedule(self):
        data = self.get_data()
        return data["EVENT_NM"]+"이(가) 있습니다."
