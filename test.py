# import filemanager as fm

# # data = fm.read_school_info("ATPT_OFCDC_SC_CODE")

# fm.writejson("school_info.json", {"school_info": "dkdk"})

# # print(data)
import filemanager as fm
import requests
url = "https://open.neis.go.kr/hub/schoolInfo"

params = {
    "KEY": fm.read_api_key("neis"),
    "Type": "json",
    "SCHUL_NM": "선린인터넷고등학교"
}

rersponse = requests.get(url, params=params)

print(rersponse.json())
params = {
    "KEY": fm.read_api_key("neis"),
    "Type": "json",
    "SCHUL_NM": "한세사이버보안고"
}

rersponse = requests.get(url, params=params)

print(rersponse.json())