import os


def data_handling():
    user_input = input("Do you want do keep items.csv? (y) for YES and (n) for NO: ")
    while True:
        if user_input == 'n':
            os.remove("items.csv")
            break
        elif user_input == 'y':
            break
        else:
            print('wrong input')