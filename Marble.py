import random
from interface import *

class User:
    def __init__(self, name, number = 4):
        self.name = name
        self.number = number

    def getName(self):
        return self.name
    
    def getNumber(self):
        return self.number
    
    def dropMarble(self):
        self.number -= 1

class Show:
    def __init__(self, player, dobby):
        self.dobby = dobby
        self.player = player
        self.result = 0 # 매턴 마다 홀짝 결과 저장
        self.expec = 0 # 매턴 홀짝 예상 값

    def prtStatus(self):
        pNumber = self.player.getNumber()
        dNumber = self.dobby.getNumber()

        clear()
        
        print("%6s"% self.player.getName() + " : ", end="")
        for i in range(pNumber):
            print("🟡", end="")
        print()
        
        print("%6s"% self.dobby.getName() + " : ", end="")
        for i in range(dNumber):
            print("🟡", end="")
        print()

    def evaluate(self):
        if self.dobby.getNumber() == 0:
            clear()
            dobby_say("주인님이 승리했어요! 🚀")
            return False
        elif self.player.getNumber() == 0:
            clear()
            dobby_say("도비가 승리했어요! 🪄")
            return False
        else:
            return True
    
    def turn(self):
        dobby_say("홀짝을 예상해주세요!\n"+
                  "  1) 홀수\n"+
                  "  2) 짝수")
        self.expec = int(my_answer())    #예상값을 입력

    def oddeven(self):
        number_list = random.choice(range(1, self.dobby.getNumber()+1))
        if number_list % 2 == 0:
            dobby_say(f"{number_list}이므로 짝수입니다!")
            self.result = 2
        else:
            dobby_say(f"{number_list}이므로 홀수입니다!")
            self.result = 1

    def count(self):
        if self.result == self.expec:    #예상에 성공한 경우 도비의 구슬이 감소
            self.dobby.dropMarble()
            dobby_say("주인님이 맞추셨어요!!\n"+
                      "도비의 구슬을 가져가셔도 좋아요....")
        
        elif self.result != self.expec:    #실패한 경우 플레이어의 구슬 감소
            self.player.dropMarble()
            dobby_say("아이쿠..주인님 틀리셨네요\n"+
                      "주인님의 구슬은 이제 제 것입니다!")


def game():
    player = User("Malfoy")
    dobby = User("Dobby")

    show = Show(player, dobby)

    show.prtStatus()

    while(show.evaluate()):
        show.turn()
        show.oddeven()
        show.count()
        petc()
        show.prtStatus()