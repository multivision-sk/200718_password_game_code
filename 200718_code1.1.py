#guessmypassword

import random

#variable initialize
response1 = "다시 시도해보세요"
response2 = "그럴듯하지만 아니에요. 다시 입력해보세요"
response3 = "내 비밀번호가 아니에요. 내 비밀번호는 정말 쉬워요"
response4 = "잘했어요"
MY_PASSWORD = "my password"
response5 = "포기하시겠습니까?"
response6 = "네"
"""
#플레이어가 입력한 비밀번호가 올바른지 확인하는 함수
def is_correct(guess, password) :
    if guess == password :
        guess_correct = True
    else :
        guess_correct = False

    return guess_correct
"""

def is_correct(guess,password) :
    return guess==password


#게임 시작
print("--------게임시작----------\n")
user_guess = input("추측한 내비밀번호를 입력하세요:")

#함수를 불러와서 비밀번호가 맞는지 확인
true_or_false = is_correct(user_guess, MY_PASSWORD)

#사용자가 입력한 비밀번호가 일치할 때까지 게임 실행

i=0
while true_or_false == False  :
    computer_response = random.randint(1,3)

    if computer_response == 1 :
        print(response1)
        i+=1
    elif computer_response == 2 :
        print(response2)
        i += 1
    elif computer_response == 3  :
        print(response3)
        i += 1



        #사용자에게 다시 비밀번호 입력 요청
    user_guess = input("\n다음 비밀번호는 무엇입니까?")

    #비밀번호가 맞는지 재확인
    true_or_false = is_correct(user_guess,MY_PASSWORD)


    print(i)

    if i>=3 :
        print(response5)
        user_response = input("입력하세요")
        if user_response == response6:
            break

#게임종료
print(response4)
input("\n\n엔터키를 눌러 종료하세요")





