from NeisApi import *

SchoolInfo(str(input("School NAME: "))).get_school_info()
print(MealService(str(input("Meal Service data: "))).get_meal_info()["DDISH_NM"].replace("<br/>", "\n"))
print(hisTimetable(str(input("학년도: ")), str(input("학기: ")), str(input("날짜: ")), str(input("학년: "))).get_timetable())


