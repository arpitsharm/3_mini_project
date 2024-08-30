import os
import time

result = 0

while True :
    print("Welcome to Simple Calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    choice = int(input("Enter your choice (1-5): "))
    if (choice == 1) or (choice == 2) or (choice == 3) or (choice == 4):
        no1 = int(input("Enter your Number 1 :-"))
        no2 = int(input("Enter your Number 2 :-"))

        if (choice == 1):
            result = no1 + no2
            print("Addition Result : ", result)
            print("Time Only 3 Seconds")
            time.sleep(3)
            os.system("cls")

        elif (choice == 2):
            result = no1 - no2
            print("Subtraction Result : ", result)
            print("Time Only 3 Seconds")
            time.sleep(3)
            os.system("cls")

        elif (choice == 3):
            result = no1 * no2
            print("Multiplication Result : ", result)
            print("Time Only 3 Seconds")
            time.sleep(3)
            os.system("cls")
        
        elif (choice == 4):
            result = no1 / no2
            print("Division Result : ", result)
            print("Time Only 3 Seconds")
            time.sleep(3)
            os.system("cls")

    elif (choice == 5):
        exit()
