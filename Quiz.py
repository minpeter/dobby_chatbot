import random
from User import User
import filemanager as fm
from interface import *

class Quiz:
    def __init__(self, player):
        self.player = player
        self.p_result = "" # 나의 퀴즈 정답
        self.result = "" # 퀴즈의 정답
        self.quiz_list = fm.read_quiz()

    def prtStatus(self):
        clear()
        print("남은 퀴즈 수 : ", end="")
        for i in range(self.player.getNumber()):
            print("🟢", end="")
        print()

        print("   현재 점수 : ", end="") #한국어줄맞춤이슈
        for i in range(self.player.getScore()):
            print("🟢", end="")
        print()

    def evaluate(self):
        if self.player.getNumber() == 0:
            clear()
            dobby_say("모든 문제를 풀었습니다 🚀\n" +
                      f"{self.player.getScore()}문제를 맞히셨군요!")
            return False
        else:
            return True

    def quiz(self): #해리포터 관련 퀴즈를 랜덤으로 출력
        random_index = random.choice(range(len(self.quiz_list)))
        dobby_say(self.quiz_list[random_index]["quiz"] + "\n" + \
                  "  1)" + self.quiz_list[random_index]["example"][0] + "\n" + \
                  "  2)" + self.quiz_list[random_index]["example"][1] + "\n" + \
                  "  3)" + self.quiz_list[random_index]["example"][2] + "\n" + \
                  "  4)" + self.quiz_list[random_index]["example"][3] + "\n")
        self.result = self.quiz_list[random_index]["answer_index"]
        del(self.quiz_list[random_index])

    def comp(self):
        self.player.dropNumber()
        dobby_say("정답은 몇번째 답인가요?")
        self.p_result = int(answer())
        if self.p_result == self.result:
            dobby_say("정답입니다!")
            self.player.addScore()
        else:
            dobby_say("오답입니다. 정답은 " + str(self.result) + "입니다.")

def game():
    player = User("Malfoy", 3)
    quiz = Quiz(player)

    quiz.prtStatus()

    while(quiz.evaluate()):
        quiz.quiz()
        quiz.comp()
        petc()
        quiz.prtStatus()

if __name__ == "__main__":
    game()