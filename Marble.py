import random

class Marble:
    def __init__(self):
        self.result = 0 # 매턴 마다 홀짝 결과 저장
        self.expec = 0 # 매턴 홀짝 예상 값
        self.dobby = 4 # 도비의 잔여 구슬 갯수
        self.player = 4 # player의 잔여 구슬 갯수

    def game(self):
        game_on = True
        while game_on:
            if self.dobby == 0:
                game_on = False
                return f"주인님이 승리했어요!\n"+self.__str__()

            elif self.player == 0:
                game_on = False
                return f"도비가 승리했어요!\n"+self.__str__()
            else:
                self.turn()
                print("==================================")
                self.oddeven()
                print("==================================")
                self.count()
                print("==================================")

    def turn(self):
        print("홀짝을 예상해주세요!")
        print("1) 홀수\n"+
              "2) 짝수")
        self.expec = int(input(">> "))    #예상값을 입력

    def oddeven(self):
        number_list = random.choice(range(1, self.dobby+1))
        if number_list % 2 == 0:
            print(f"{number_list}이므로 짝수입니다!")
            self.result = 2
        else:
            print(f"{number_list}이므로 홀수입니다!")
            self.result = 1

    def count(self):
        if self.result == self.expec:    #예상에 성공한 경우 도비의 구슬이 감소
            self.dobby -= 1
            print("주인님이 맞추셨어요!!")
            print("도비의 구슬을 가져가셔도 좋아요....")
        
        elif self.result != self.expec:    #실패한 경우 플레이어의 구슬 감소
            self.player -= 1
            print("아이쿠..주인님 틀리셨네요")
            print("주인님의 구슬은 이제 제 것입니다!")

    def __str__(self):
        return f"도비의 구슬은 {self.dobby}개 입니다."+\
               f"\n플레이어의 구슬은 {self.player}개 입니다."

if __name__ == "__main__":
    Marble().game()