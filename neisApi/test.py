# import filemanager as fm

# # data = fm.read_school_info("ATPT_OFCDC_SC_CODE")

# fm.writejson("school_info.json", {"school_info": "dkdk"})

# # # print(data)
# import filemanager as fm
# import requests
# url = "https://open.neis.go.kr/hub/schoolInfo"

# params = {
#     "KEY": fm.read_api_key("neis"),
#     "Type": "json",
#     "SCHUL_NM": "선린인터넷고등학교"
# }

# rersponse = requests.get(url, params=params)

# print(rersponse.json())
# params = {
#     "KEY": fm.read_api_key("neis"),
#     "Type": "json",
#     "SCHUL_NM": "한세사이버보안고"
# }

# rersponse = requests.get(url, params=params)

# print(rersponse.json())

test_str = "기장밥<br/>매콤버섯찌개5.6.13.<br/>참나물새콤겉절이5.6.13.<br/>소불고기(떡)5.6.8.13.16.18.<br/>부추전/초간장1.5.6.13.<br/>배추겉절이(완)9.13."
print(test_str.replace("<br/>", "\n"))