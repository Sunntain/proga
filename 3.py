def z1():
 st = []
 while (st1 := str(input())) != "stop":
     st.append(st1)
 print(" ".join(st))


def z2():
 sl = []
 while (s := str(input())) != "stop":
     if "ф" in s or "Ф" in s:
         print("редкое слово")
     else:
         print("не редкое слово")

def z3():
 from random import randint
 import sys
 kp = 0
 knp = 0
 while knp != 3:
   while True:
     x = randint(1,50)
     y = randint(1,50)
     print(f" {x} + {y} = ", end="")
     r = input()
     if r == "stop":
         print('игра закончена, верных ответов: ', kp)
         sys.exit()
     r = int(r)
     if x+y==r:
         kp+=1
     else:
         print('ошибка')
         knp+=1
     if knp == 3:
         print('3 ошибки, игра окончена, верных ответов: ', kp)
         break

z3()