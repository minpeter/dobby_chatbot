import random
from User import User
from interface import *

class Rsp:
    def __init__(self, player, dobby):
        self.dobby = dobby
        self.player = player
        self.d_rsp = "" # 매턴 마다 홀짝 결과 저장
        self.p_rsp = "" # 매턴 홀짝 예상 값

    def prtStatus(self):
        pNumber = self.player.getNumber()
        dNumber = self.dobby.getNumber()

        clear()
        
        print("%6s"% self.player.getName() + " : ", end="")
        for i in range(pNumber):
            print("🟠", end="")
        print()
        
        print("%6s"% self.dobby.getName() + " : ", end="")
        for i in range(dNumber):
            print("🟠", end="")
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
    
    def comp(self):
        dobby_say("가위, 바위, 보 중 하나를 입력해주세요!\n"+
                  "  1) 가위\n"+
                  "  2) 바위\n"+
                  "  3) 보")
        self.p_rsp = int(answer())
        self.d_rsp = random.choice(range(1, 3+1))

    def rsp_comp(self):
        if self.d_rsp == self.p_rsp:
            dobby_say("이런..! 주인님이랑 비겨버렸네요..\n")

        elif self.p_rsp==1 and self.d_rsp==3 or \
                self.p_rsp==2 and self.d_rsp==1 or \
                    self.p_rsp==3 and self.d_rsp==2:
            self.dobby.dropNumber()
            dobby_say("주인님이 이겼어요! 🚀")

        elif self.p_rsp==1 and self.d_rsp==2 or \
                self.p_rsp==2 and self.d_rsp==3 or \
                    self.p_rsp==3 and self.d_rsp==1:
            self.player.dropNumber()
            dobby_say("도비가!! 도비가 이겼어요!! 🪄")
        else:
            dobby_say("다시 한번 입력해 주세요...!")

def game():
    player = User("Malfoy", 3)
    dobby = User("Dobby", 3)

    rsp = Rsp(player, dobby)

    rsp.prtStatus()

    while(rsp.evaluate()):
        rsp.comp()
        rsp.rsp_comp()
        petc()
        rsp.prtStatus()

if __name__ == "__main__":
    game()