import os

def dobby_say(msg):
    print(f"Dobby: {msg}".replace('\n', '\n       '))
    # 도비가 출력하는 메세지가 여러줄로 이루어졌을 경우
    # 첫줄과 함께 출력되는 Dobby: ~~ 와 간격의 위해 \n을 \n과 7칸의 공백으로 대체함

def answer():
    return input("Malfoy: ")

def petc():  #press enter to continue
    print()
    input("Press Enter to continue...")
#while문 사용시 clear로 인해 텍스트가 사라지는걸 방지하는 함수

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)