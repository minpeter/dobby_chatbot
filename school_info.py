import requests
from readfile import readfile

URL = "https://open.neis.go.kr/hub/schoolInfo"
params = {
    #기본인자
    "KEY": readfile(".api_key"),
    "Type": "json",
    "pindex": "1",
    "pSize": "10",
    #신청인자
    "SCHUL_NM": "한세사이버보안고"
}
response = requests.get(URL, params=params)
print(response.text)
