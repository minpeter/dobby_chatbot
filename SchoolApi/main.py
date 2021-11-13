from SchoolApi import SchoolApi

params = {
    "SCHUL_NM": str(input("학교명(fullname) : ")),
}

SchoolApi("schoolInfo", params).get_school_info()

params = {
    "MLSV_YMD":  str(input("급식일자(YYYYMMDD) : ")),
}

mealservice = SchoolApi("mealServiceDietInfo", params)

print(mealservice.get_data())

params = {
    "ALL_TI_YMD":  str(input("시간표일자(YYYYMMDD) : ")),
    "GRADE":  str(input("학년 : ")),
    "CLASS_NM":  str(input("반명 : "))
}

histimetable = SchoolApi("hisTimetable", params)

print(histimetable.get_data())

params = {
    "AA_YMD":  str(input("학사일자(YYYYMMDD) : "))
}

schoolschedule = SchoolApi("SchoolSchedule", params)

print(schoolschedule.get_data())
