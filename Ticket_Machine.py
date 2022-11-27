
from venv import logger
# Python Project 1
print("Drugstore Ticket Machine")
c=0
p1=0
p=0
def visiplace():
    if visit=="c":
        global c
        c+=1
        print(f"c-{c}")
    if visit == "p":
        global p
        p += 1
        print(f"p-{p}")
    if visit == "ph":
         global p1
         p1 += 1
         print(f"p1-{p1}")

id_list = [123456,14789]
count = 0
count_limit = 3

while count_limit > count:
    id_number = int(input("please enter id_number:"))
    if id_number in id_list:
        visit = input("please enter your vist: ")
        while visit != "":
            print("your number is:")
            visiplace()
            print("please waite some one to assit you: ")
            permission = input("do you want to continue? y/n:")
            if permission == "y" or permission == "Y":
               visit = input("please enter your vist: ")
            else:
                print()
                exit(0)

    count+=1
else:
  print("your chose is incorrect")