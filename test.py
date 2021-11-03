
import requests
from readfile import readfile
import urllib3

urllib3.disable_warnings() # Disable SSL warnings
URL = "https://open.neis.go.kr/hub/schoolInfo"
params = {
    #기본인자
    "KEY": readfile(".api_key"),
    "Type": "json",
    #신청인자
    "SCHUL_NM": "한세사이버보안고",
    "SD_SCHUL_CODE": None
}
response = requests.get(URL, params=params, verify=False)
print(response.text)


# url = "https://open.neis.go.kr/hub/schoolInfo"
# params = {
#     #기본인자
#     "KEY": readfile(".api_key"),
#     "Type": "json",
#     #신청인자
#     "SCHUL_NM": "한세사이버보안고"
# }
# school_info = NeisApi(url, params)

# url = "https://open.neis.go.kr/hub/mealServiceDietInfo"
# params = {
#     #기본인자
#     "KEY": readfile(".api_key"),
#     "Type": "json",
#     #신청인자
#     "ATPT_OFCDC_SC_CODE": "B10",
#     "SD_SCHUL_CODE": "7010911",
#     "MLSV_YMD":"20211103"
# }
# meal_service = NeisApi(url, params)

# print(school_info.get_data())
# print(meal_service.get_data())
