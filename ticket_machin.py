def drug_store():
    id_list = [123456, 14789]
    count = 0
    count_limit = 3
    while count_limit > count:
        id_number = int(input("please enter id_number:"))
        if id_number in id_list:
            visit = input("please enter your vist: ")
            while visit != "":
                print("your number is:", visit)

                print("please waite someone to assit you: ")
                permission = input("do you want to continue? y/n:")
                if permission == "y" or permission == "Y":
                    visit = input("please enter your vist: ")

                else:
                    print("Timer ended!")
                    print()
                    exit(0)
        count += 1
    else:
        print("your chose is incorrect")