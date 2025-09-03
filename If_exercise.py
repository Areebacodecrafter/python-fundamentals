temp = int(input("Enter temprature  in celcius"))
if temp <= 0:
    print("Warning! Low temprature")
elif temp > 0 and  35:
    print("Tempratur is normal")
else:
    print("Warning! High temprature")


#QUESTION NO 4
days = int(input("Enter number of days"))
if (days == 28 or days == 29):
    print("FEB")
elif (days == 30):
    print("APR, JUN, SEP, NOV")
elif (days == 31):
    print("Mar, May, Jul, Aug, Oct, Dec")
else:
    print("ERROR")


# QUESRION 5
length = input("Enter length in foots")
input(" In which unit do you want to covert the lenght, meters, centimeters or inches? ")
if length == "inches":
    print(length/12)
elif length== "centimeters":
    print(length/30.48)
elif length == "meters":
    print(length/.3048)
else:
    print("ERROR")


#QUESTIONS 6
number = int(input("Enter a number between 20 to 99"))
if number >= 20 and number<=90:
    if number >19 and number <30:
        print("veinte")
    elif number > 29 and number <40:
        print("treinta")
    elif number >39 and number <50:
        print(" cincuenta")
    elif number > 49 and number <60:
        print("sesenta")
    elif number >59 and number< 70:
        print(" ")
    elif number >69 and number <80:
        print("setenta")
    elif number >79 and number < 90:
        print("ochenta")
    elif number >89 and number <100:
        print("noventa")
else:
    print("Error")   


    #QUESTIONB 7
a = int(input("enter a number"))
if not((a == 0 or a == 2 or a == 5) or (a > 10 and a < 15) or (a > 20 and a < 25)):
    print("OKAYYYYY")

# QUESTION 8
word = input("ENTER YOUR CHARACTER")
if word == 'n':
    print("creating a new doc")
else:
    if word == 'o':
        print("opening a new doc")
    else:
        if word == 's':
            print("saving a new file")
        else:
            if word == 'x':
                print("exiting the mew file")
            else:
                print("invalid option")
            

import random

num = random.choices([0, 1], weights=[2, 1])[0] # 0 will be twice 1's

print(num)


i = 0
for x in range(200):
    if i % 10 != 8:
        print(f"file{i}.jpg")
        i +=1

