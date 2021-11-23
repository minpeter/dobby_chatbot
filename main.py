from SchoolApi import SchoolApi
from Rsp import Rsp
from Quiz import quiz
import random
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
    "SCHUL_NM": str(input("주인님이 찾으시는 학교명을 입력해주세요!!(fullname) : ")),
}

while not quit:
    SchoolApi("schoolInfo", params).get_school_info()

    dobby_say("무엇을 하실껀가요, 주인님?")
    msg = my_answer()

    if "급식" in msg:
        dobby_say("급식말입니까? 알겠습니다!\n"+
                "  1) 주인님의 오늘 급식은 이쪽입니다.\n"+
                "  2) 내일 급식을 보고싶으시다면 이쪽입니다!\n"+
                "  3) 직접 날짜를 입력하고 싶으시면 이쪽으로 와주세요!")
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
        dobby_say("시간표을 알고싶으시다고요?")
        params = {
            "ALL_TI_YMD":  str(input("시간표일자(YYYYMMDD) : ")),
            "GRADE":  str(input("학년 : ")),
            "CLASS_NM":  str(input("반명 : "))
        }
        dobby_say(SchoolApi("hisTimetable", params).get_data())

    elif "학사" in msg or "일정" in msg:
        dobby_say("학사일정을 알려드리겠습니다, 주인님\n"+
                "  1) 오늘 학사일정은 여기서 확인해주세요!\n"+
                "  2) 내일 학사일정은 이쪽에서 도와드리겠습니다, 주인님\n"+
                "  3) 직접 날짜 입력하실려면 여기에서 도와드리도록 하죠")

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
        dobby_say("도비에게 도움을 구하고 싶으긴가요?\n"+
                "급식을 알고싶으시면 급식을 입력해주세요\n"+
                "시간표를 알고싶으시면 시간표를 입력해주세요\n"+
                "학사일정을 알고싶으시면 학사일정을 입력해주세요\n"+
                "저와 게임을 하고 싶으시다면 게임을 입력해주세요!\n"+
                "양말을 주면, 도비는 무료가 되요!")
    

    elif "양말" in msg or "socks" in msg or "돌아가" in msg:
        bye = ['도비는 자유에요!','도비는 이제 떠날 수 있어요!','도비는 떠날거에요!','주인님이 저에게 양말을 주셨어요! 아무도 도비를 속박하지 못해','이제 아무도 도비를 속박하지 못해요!']
        dobby_say(random.choice(bye))
        quit = True

    elif "하이" in msg or "안녕" in msg:
        hi = ['반갑습니다..도비에요..','도비입니다..','왔습니다, 주인님!','주인님 도비랑 놀아주세요','안녕하세요 주인님']
        dobby_say(random.choice(hi))

    elif "게임" in msg or "놀" in msg or "심심해" in msg:
        dobby_say("좋습니다! 도비랑 게임 하나 하시죠..!\n"+
                "  1) 도비와 가위-바위-보\n"+
                "  2) 도비와 함께 하는 해리포터 퀴즈!\n"+
                "  3) 도비와 구슬 홀짝 미니게임")
        ## 게임 시작 부분 - 여기에 게임 코드를 작성하세요
        answer = int(my_answer())
        if answer == 1:
            dobby_say(Rsp().rsp_result())
        elif answer == 2:
            dobby_say(quiz())
        elif answer == 3:
            dobby_say("아직은 준비중이예요 :)")

    else:
        dobby_say("도비는 그런건 할 줄 몰라요 \n - 도움말을 입력해 알아보아요 :)")
