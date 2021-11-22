from SchoolApi import SchoolApi
from Rsp import Rsp
from datetime import datetime as dt
from datetime import timedelta as td

def dobby_say(msg):
    print(f"Dobby: {msg}".replace('\n', '\n       '))
    # 도비가 출력하는 메세지가 여러줄로 이루어졌을 경우
    # 첫줄과 함께 출력되는 Dobby: ~~ 와 간격의 위해 \n을 \n과 7칸의 공백으로 대체함

# def dobby_say_with_api(msg):
#     dobby_say(SchoolApi.get_reply(msg))

def my_answer():
    return input("me: ")

dobby_say("도비 일어났어요!! 뿌우📣")
quit = False
params = {
    "SCHUL_NM": str(input("학교명(fullname) : ")),
}

while not quit:
    SchoolApi("schoolInfo", params).get_school_info()

    dobby_say("무엇을 하시겠습니다?")
    msg = my_answer()

    if "급식" in msg:
        dobby_say("급식을 선택하셨습니다\n"+
                "  1) 오늘 급식 보기\n"+
                "  2) 내일 급식 보기\n"+
                "  3) 직접 날짜 입력하기")

        answer = int(my_answer())
        if answer == 1:
            dobby_say("오늘의 급식은!")
            params={"MLSV_YMD": dt.now().strftime("%Y%m%d")}
        elif answer == 2:
            dobby_say("내일의 급식은!")
            params={"MLSV_YMD": (dt.now()+td(1)).strftime("%Y%m%d")}
        elif answer == 3:
            dobby_say("어느날의 급식이 알고 싶으세요? (YYYYMMDD)")
            params = {
                "MLSV_YMD":  str(my_answer()),
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

    elif "학사" in msg or "일정" in msg:
        dobby_say("학사일정을 선택하셨습니다\n"+
                "  1) 오늘 학사일정 보기\n"+
                "  2) 내일 학사일정 보기\n"+
                "  3) 직접 날짜 입력하기")

        answer = int(my_answer())
        if answer == 1:
            dobby_say("오늘의 학사일정은!")
            params={"AA_YMD": dt.now().strftime("%Y%m%d")}
        elif answer == 2:
            dobby_say("내일 학사일정은!")
            params={"AA_YMD": (dt.now()+td(1)).strftime("%Y%m%d")}
        elif answer == 3:
            dobby_say("어느날의 학사일정이 알고 싶으세요? (YYYYMMDD)")
            params = {
                "AA_YMD":  str(my_answer()),
            }
        dobby_say(SchoolApi("SchoolSchedule", params).schedule())

    elif "도와줘" in msg or "도움말" in msg or "help" in msg:
        dobby_say("도움말을 선택하셨습니다\n"+
                "급식을 알고싶으시면 급식을 입력하세요\n"+
                "시간표를 알고싶으시면 시간표를 입력하세요\n"+
                "학사일정을 알고싶으시면 학사일정을 입력하세요\n"+
                "양말을 주면, 도비는 무료가 되요!")
    
    elif "양말" in msg or "exit" in msg or "quit" in msg:
        dobby_say("양말을 도비에게 주었어요\n도비는 자유에요")
        quit = True

    elif "게임" in msg or "놀" in msg or "심심해" in msg:
        dobby_say("좋습니다! 도비랑 게임 하나 하시죠..!")
        ## 게임 시작 부분 - 여기에 게임 코드를 작성하세요
        dobby_say(Rsp().rsp_result())

    else:
        dobby_say("도비는 그런건 할 줄 몰라요 \n - 도움말을 입력해 알아보아요 :)")
