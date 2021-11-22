import random

class Rsp:
    def __init__(self):
        self.p_rsp = input("가위, 바위, 보 중 하나를 입력해주세요!: ")
        self.d_rsp = random.choice(["가위", "바위", "보"])

        if (self.p_rsp=="가위" and self.d_rsp=="보") or (self.p_rsp=="바위" and self.d_rsp =="가위") or (self.p_rsp=="보" and self.d_rsp=="바위") :
            self.result_msg = f"주인님은 {self.p_rsp}, 도비는 {self.d_rsp}, 주인님의 승리입니다..! 역시 그럴 줄 알았어요..!"
        elif (self.p_rsp=="가위" and self.d_rsp=="가위") or (self.p_rsp=="바위" and self.d_rsp =="바위") or (self.p_rsp=="보" and self.d_rsp=="보") :
            self.result_msg = f"주인님은 {self.p_rsp}, 도비는 {self.d_rsp}, 이런..! 주인님이랑 비겨버렸네요.."
        elif (self.p_rsp=="가위" and self.d_rsp=="바위") or (self.p_rsp=="바위" and self.d_rsp =="보") or (self.p_rsp=="보" and self.d_rsp=="가위") :
            self.result_msg = f"주인님은 {self.p_rsp}, 도비는 {self.d_rsp}, 도비가!! 도비가 이겼어요!!"
        else:
            self.result_msg = "다시 한번 입력해 주세요..!."

    def rsp_result(self):
        return self.result_msg