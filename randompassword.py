import random

Dicth="1234567890!@#$%^&*()_+-=abcdefghijklmnopqrstuvwxyz"
Pass_Temp = []
Pass_Exam = ''

# def Password_Length():
#     P_Length = int(input())
#     retrun P_Length

# def Password_Come(P_temp):
#     exam = []
#     for i in range(P_temp):
#         exam.append(random.choice(Dicth))
#     retrun exam

if __name__ == '__main__':
    P_Length = int(input())
    for i in range(P_Length):
        Pass_Temp.append(random.choice(Dicth))
    Pass_Exam = ''.join(Pass_Temp)
    print(Pass_Exam)
    
