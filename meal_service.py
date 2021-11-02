import requests
from readfile import readfile

URL = "https://open.neis.go.kr/hub/mealServiceDietInfo"
params = {
    #기본인자
    "KEY": readfile(".api_key"),
    "Type": "json",
    "pindex": "1",
    "pSize": "10",
    #신청인자
    "ATPT_OFCDC_SC_CODE": "B10",
    "SD_SCHUL_CODE": "7010911",
    # "SCHUL_SC_CODE": "B100000662",
    # "SCHUL_KIND_CODE": "4",
    # "SCHUL_SC_NM": "서울시청",
    "MLSV_YMD":"20211103"
}
response = requests.get(URL, params=params)
print(response.text)
