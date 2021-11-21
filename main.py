from SchoolApi.SchoolApi import SchoolApi

def dobby_say(msg):
    print(f'Dobby: {msg}')

print("---------Dobby Online---------")

params = {
    "SCHUL_NM": str(input("학교명(fullname) : ")),
}

SchoolApi("schoolInfo", params).get_school_info()

dobby_say("무엇을 하시겠습니다?")
msg = input("me: ")

if msg == "급식":
    dobby_say("급식을 선택하셨습니다")
    params = {
        "MLSV_YMD":  str(input("급식일자(YYYYMMDD) : ")),
    }
    print(SchoolApi("mealServiceDietInfo", params).get_data())

elif msg == "시간표":
    dobby_say("시간표을 선택하셨습니다")
    params = {
        "ALL_TI_YMD":  str(input("시간표일자(YYYYMMDD) : ")),
        "GRADE":  str(input("학년 : ")),
        "CLASS_NM":  str(input("반명 : "))
    }
    print(SchoolApi("hisTimetable", params).get_data())

elif msg == "학사일정":
    dobby_say("학사일정을 선택하셨습니다")
    params = {
        "AA_YMD":  str(input("학사일자(YYYYMMDD) : "))
    }
    print(SchoolApi("SchoolSchedule", params).get_data())

elif msg == "도움말":
    dobby_say("도움말을 선택하셨습니다")
else:
    dobby_say("알 수 없는 명령어 입니다")


