from SchoolApi.SchoolApi import SchoolApi
from game.Rsp import Rsp

def dobby_say(msg):
    print(f'Dobby: {msg}')

dobby_say("도비 일어났어요!!\n 도비는 공짜에요.")
quit = False
params = {
    "SCHUL_NM": str(input("학교명(fullname) : ")),
}

while not quit:
    SchoolApi("schoolInfo", params).get_school_info()

    dobby_say("무엇을 하시겠습니다?")
    msg = input("me: ")

    if "급식" in msg:
        dobby_say("급식을 선택하셨습니다")
        params = {
            "MLSV_YMD":  str(input("어느날의 급식을 알고 싶으세요? (YYYYMMDD) : ")),
        }
        dobby_say(SchoolApi("mealServiceDietInfo", params).meal())

    elif "시간표" in msg:
        dobby_say("시간표을 선택하셨습니다")
        params = {
            "ALL_TI_YMD":  str(input("시간표일자(YYYYMMDD) : ")),
            "GRADE":  str(input("학년 : ")),
            "CLASS_NM":  str(input("반명 : "))
        }
        dobby_say(SchoolApi("hisTimetable", params).get_data())

    elif "학사일정" in msg:
        dobby_say("학사일정을 선택하셨습니다")
        params = {
            "AA_YMD":  str(input("학사일자(YYYYMMDD) : "))
        }
        dobby_say(SchoolApi("SchoolSchedule", params).schedule())

    elif "도와줘" in msg or "도움말" in msg or "help" in msg:
        dobby_say("도움말을 선택하셨습니다\n"+
        "급식을 알고싶으시면 급식을 입력하세요\n"+
        "시간표를 알고싶으시면 시간표를 입력하세요\n"+
        "학사일정을 알고싶으시면 학사일정을 입력하세요\n"+
        "종료하려면 양말을 입력하세요")
    
    elif "양말" in msg or "exit" in msg or "quit" in msg:
        dobby_say("양말을 도비에게 주었어요\n도비는 자유에요")
        quit = True

    elif "게임" in msg or "놀" in msg or "심심해" in msg:
        dobby_say("좋습니다! 도비랑 게임 하나 하시죠..!")
        ## 게임 시작 부분 - 여기에 게임 코드를 작성하세요
        dobby_say(Rsp().rsp_result())

    else:
        dobby_say("도비는 그런건 할 줄 몰라요 \n - 도움말을 입력해 알아보아요 :)")
