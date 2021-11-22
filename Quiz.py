import random

def quiz():
    eng_word = [["해리는 볼드 모트 경을 죽이기 위해 사용한", "엑스펠리아르무스"], ["잠겨 있는 문을 열수있는", "알로호모라"], ["헤르미온느가 부모님의 기억을 지울 때 시용했던", "오블리비아테"], ["믈건을 조립할 때 사용하는", "에렉토"], ["물건을 소환하는", "아씨오"], ["물건을 복제하는", "제미니오"], ["사물이나 사람을 밀칠 때 쓰는", "아라니아 엑서메이"]]

    quiz_on = True
    score = 0
    quiz_num = 0

    while quiz_on:
        quiz_num += 1
        multi_choice = random.sample(eng_word, 4)
        answer_index = random.randint(0, 3)

        print(f"문제{quiz_num}번.{multi_choice[answer_index][0]} 주문은 무엇일까요...?")

        for i in range(4):
            print(f"{i + 1}. {multi_choice[i][1]}")

        print()
        user_input = int(input("정답을 적어주세요!!. 종료: 0>>>>  "))

        if user_input == 0:
            quiz_on = False
            print("퀴즈가 끝났습니다~.")
            print(f"총 {quiz_num-1}문제 중 {score}문제를 맞히셨군요!!")
        elif user_input == answer_index + 1:
            score += 1
            print("정답이에요!!.")
        else:
            print(f"아쉽게도 오답이네요. 정답은 {answer_index + 1}번 이에요~!.")
        print()