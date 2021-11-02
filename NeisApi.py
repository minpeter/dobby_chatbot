import requests
from readfile import readfile

class NeisApi:
    def __init__(self, url, type="json"):
        self.url = url
        self.params = {
            "KEY": readfile(".api_key"),
            "Type": type
        }


    def get_data(self):
        response = requests.get(self.url, params=self.params)
        return response.text


# https://open.neis.go.kr/hub/schoolInfo
# 학교기본정보

class SchoolInfo(NeisApi):
    def __init__(self):
        pass

# https://open.neis.go.kr/hub/mealServiceDietInfo
# 급식식단정보

class MealService(NeisApi):
    def __init_(self):
        pass

# https://open.neis.go.kr/hub/SchoolSchedule
# 고등학교시간표

class SchoolSchedul(NeisApi):
    def __init__(self):
        pass

#  https://open.neis.go.kr/hub/acaInsTiInfo
# 학사일정

class AcaInsTiInfo(NeisApi):
    def __init__(self):
        pass