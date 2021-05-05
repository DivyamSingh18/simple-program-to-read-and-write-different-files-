#This program is used by a person to write and read data from different files

import datetime

def gettime():
    return datetime.datetime.now()

q1 = int(input("> Press 1 to Input Data\t> Press 2 to Retrieve Data\n"))

if q1==1:
    iq1 = int(input("> Press 1 for Labham > Press 2 for Danish > Press 3 for Divyam\n"))
    if iq1 == 1:
        iq2 = int(input("> Press 1 for Exercise\t > Press 2 for Food\n"))
        if iq2 == 1:
            with open("Labham-exercises-done.txt", "a") as l:
                l.write( "["+str(gettime())+"] :"+ input("Type Here"))
                print('Data added successfully')
        elif iq2 == 2:
            with open("Labham-food-eaten.txt", "a") as l:
                l.write( "["+str(gettime())+"] :"+ input("Type Here"))
                print('Data added successfully')
        else:
            print('Invalid Input')

    elif iq1 == 2:
        iq2 = int(input("> Press 1 for Exercise\t > Press 2 for Food\n"))
        if iq2 == 1:
            with open("Danish-exercises-done.txt", "a") as l:
                l.write( "["+str(gettime())+"] :"+ input("Type Here"))
                print('Data added successfully')
        elif iq2 == 2:
            with open("Danish-food-eaten.txt", "a") as l:
                l.write( "["+str(gettime())+"] :"+ input("Type Here"))
                print('Data added successfully')
        else:
            print('Invalid Input')

    elif iq1 == 3:
        iq2 = int(input("> Press 1 for Exercise\t > Press 2 for Food\n"))
        if iq2 == 1:
            with open("Divyam-exercises-done.txt", "a") as l:
                l.write("[" + str(gettime()) + "] :" + input("Type Here"))
                print('Data added successfully')
        elif iq2 == 2:
            with open("Divyam-food-eaten.txt", "a") as l:
                l.write("[" + str(gettime()) + "] :" + input("Type Here"))
                print('Data added successfully')
        else:
            print('Invalid Input')
    else:
        print("Invalid Input")

elif q1==2:
    iq1 = int(input("> Press 1 for Labham > Press 2 for Danish > Press 3 for Divyam\n"))
    if iq1 == 1:
        iq2 = int(input("> Press 1 for Exercise\t > Press 2 for Food\n"))
        if iq2 == 1:
            with open("Labham-exercises-done.txt", "r") as l:
                print('The Data is as Follows:\n')
                print(l.read())
        elif iq2 == 2:
            with open("Labham-food-eaten.txt", "r") as l:
                print('The Data is as Follows:\n')
                print(l.read())
        else:
            print('Invalid Input')

    elif iq1 == 2:
        iq2 = int(input("> Press 1 for Exercise\t > Press 2 for Food\n"))
        if iq2 == 1:
            with open("Danish-exercises-done.txt", "r") as l:
                print('The Data is as Follows:\n')
                print(l.read())
        elif iq2 == 2:
            with open("Danish-food-eaten.txt", "r") as l:
                print('The Data is as Follows:\n')
                print(l.read())
        else:
            print('Invalid Input')

    elif iq1 == 3:
        iq2 = int(input("> Press 1 for Exercise\t > Press 2 for Food\n"))
        if iq2 == 1:
            with open("Divyam-exercises-done.txt", "r") as l:
                print('The Data is as Follows:\n')
                print(l.read())
        elif iq2 == 2:
            with open("Divyam-food-eaten.txt", "r") as l:
                print('The Data is as Follows:\n')
                print(l.read())
        else:
            print('Invalid Input')
    else:
        print("Invalid Input")

else:
    print('Invalid Input')