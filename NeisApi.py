import requests
import json
from readfile import readfile
import urllib3 # for disabling SSL warnings

urllib3.disable_warnings() # Disable SSL warnings

class NeisApi:
    def __init__(self, url, type='json'):
        self.url = url
        params = {
            #기본인자
            "KEY": readfile(".api_key"),
            "Type": type
        }
        print(params)

    def get_data(self, params):
        response = requests.get(self.url, params=params, verify=False)
        return response.text
    
    def data_refine(self, response_text, refine_key):
        refine_data = json.loads(response_text)[refine_key][1]["row"][0]
        return refine_data
    
    @classmethod
    def add_params(cls, params_key, params_value):
        cls.params[params_key] = params_value
        return 0

    @classmethod
    def update_school_info(cls, atpt_ofcdc_sc_code, sd_schul_code):
        cls.params["ATPT_OFCDC_SC_CODE"] = atpt_ofcdc_sc_code
        cls.params["SD_SCHUL_CODE"] = sd_schul_code
    
    

# https://open.neis.go.kr/hub/schoolInfo
# 학교기본정보

class SchoolInfo(NeisApi):
    def __init__(self, schul_nm):
        URL = "https://open.neis.go.kr/hub/schoolInfo"
        super().__init__(URL)
        self.schul_nm = schul_nm

    def get_school_info(self):
        
        params = NeisApi.add_params("schulNm", self.schul_nm)
        response_text = self.get_data(params)
        data = self.data_refine(response_text, "schoolInfo")
        NeisApi.update_school_info(data["ATPT_OFCDC_SC_CODE"], data["SD_SCHUL_CODE"])

# https://open.neis.go.kr/hub/mealServiceDietInfo
# 급식식단정보

class MealService(NeisApi):
    def __init__(self, mlsv_ymd):
        URL = "https://open.neis.go.kr/hub/mealServiceDietInfo"
        super().__init__(URL)
        self.mlsv_ymd = mlsv_ymd

        #신청인자
        NeisApi.params['MLSV_YMD'] = self.mlsv_ymd
    
    def get_meal_info(self):
        response_text = self.get_data()
        print(response_text) # for debugging
        
        data = self.data_refine(response_text, "mealServiceDietInfo")
        return data

# https://open.neis.go.kr/hub/SchoolSchedule
# 고등학교시간표

class SchoolSchedul(NeisApi):
    def __init__(self, atpt_ofcdc_sc_code, sd_schul_code):
        URL = "https://open.neis.go.kr/hub/SchoolSchedule"
        super().__init__(URL)
        self.atpt_ofcdc_sc_code = atpt_ofcdc_sc_code
        self.sd_schul_code = sd_schul_code

        #신청인자
        NeisApi.params['ATPT_OFCDC_SC_CODE'] = self.atpt_ofcdc_sc_code
        NeisApi.params['SD_SCHUL_CODE'] = self.atpt_ofcdc_sc_code

#  https://open.neis.go.kr/hub/acaInsTiInfo
# 학사일정

class AcaInsTiInfo(NeisApi):
    def __init__(self, atpt_ofcdc_sc_code, sd_schul_code):
        URL = "https://open.neis.go.kr/hub/acaInsTiInfo"
        super().__init__(URL)
        self.atpt_ofcdc_sc_code = atpt_ofcdc_sc_code
        self.sd_schul_code = sd_schul_code

        #신청인자
        NeisApi.params['ATPT_OFCDC_SC_CODE'] = self.atpt_ofcdc_sc_code
        NeisApi.params['SD_SCHUL_CODE'] = self.atpt_ofcdc_sc_code