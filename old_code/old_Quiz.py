import random
from interface import *

def game():
    eng_word = [["해리는 볼드 모트 경을 죽이기 위해 사용한", "엑스펠리아르무스"], \
                ["잠겨 있는 문을 열수있는", "알로호모라"], ["헤르미온느가 부모님의 기억을 지울 때 시용했던", "오블리비아테"], \
                ["믈건을 조립할 때 사용하는", "에렉토"], ["물건을 소환하는", "아씨오"], ["물건을 복제하는", "제미니오"], \
                ["사물이나 사람을 밀칠 때 쓰는", "아라니아 엑서메이"]]

    quit = False
    score = 0
    quiz_num = 0

    while not quit:
        quiz_num += 1
        multi_choice = random.sample(eng_word, 4)
        answer_index = random.randint(0, 3)

        dobby_say(f"문제{quiz_num}번\n{multi_choice[answer_index][0]} 주문은 무엇일까요...?")

        for i in range(4):
            print(f"\t {i + 1}. {multi_choice[i][1]}")

        dobby_say("정답은 몇번째 답인가요? - 종료하실려면 \"0\"을 입력해주세요.")
        user_input = int(answer())

        if user_input == 0:
            quit = True
            dobby_say("퀴즈가 끝났습니다~\n"+
                      f"총 {quiz_num-1}문제 중 {score}문제를 맞히셨군요!!")
        elif user_input == answer_index + 1:
            score += 1
            dobby_say("정답이에요!!")
        else:
            dobby_say(f"아쉽게도 오답이네요. 정답은 {answer_index + 1}번 이에요~!")

if __name__ == "__main__":
    game()