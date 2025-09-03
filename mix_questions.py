# import random
# count = 0
# for x in range (0,50):
#     temp = random.randint(1,9)
#     print(temp, end = " ")
#     if temp == 5:
        # count = count +1


# import math

# total = 0
# for x in range(1, 101):
#     total += math.sin(x)

# print("The sum of sines from 1 to 100 is:", total)

#QUESTION


# total = 0
# for x in range(1,1000,2):
#     total += x

# print(total)

# x = int(input("Value of x: "))
# y = int(input("value of y:"))
# z = int(input("value of z:"))
# w = int(input("value of w:"))
# if x > y:
#     sml1 = y
# else:
#     sml1 = "x"
#     if y > z:
#         sml2 = "z"
#     else: 
#         sml2 = "y"
#         sml1,sml2 =sml2,sml1

# print(x, y, z, w)

# n = int(input("Enter a number n:"))
# # a,b = 1,1
# print(a,b , end= " ")

# for x in range(n-2):
#     c = b*2+a
#     print(c)
#     a,b = b,c

# n = int(input(" enter the terms on n:"))
# a,b,c = 1,2,3
# print(a,b,c, end=" ")

# for x in range(n-3):
#     d = (a+b+c)/3
#     print(round(d,3))
#     a,b,c= b,c,d




# smallnum= 0
# for x in range(10):
#        num = int(input("Enter 10 numbers between to 100:"))
#        if num >=50 and num <= 100:
#         if num < smallnum:
#             smallnum = num
#             print(smallnum)


    
# # QUESTION 1
# print("""     
#                *
#              *   *
#            *       *
#          *           *
#        *               *
#      *                   *
#     * * * * * * * * * * * *   
#     *                     * 
#     *                     *
#     *                     *
#     *                     *
#     *                     *
#     * * * *         * * * *    """)


#QUESTION 2
# fstd = str(input(" Enter your first name:") )
# lstd = str(input("Enter your last name:"))
# stdId = int(input("Enter tou ID number:"))  
 
# print(f"""Student: {fstd} {lstd},
# ID:{stdId}
# "Welcome to python Progamming!  """)



#QUESTION3
# item1 = int(input("Enter cost of item1:"))
# item2 = int(input("Enter cost of item2:"))
# item3 = int(input("Enter cost of item3:"))
# subtotal = (item1 + item2 + item3)
# print(f"subtotal: {subtotal}")
# print((subtotal*0.085)+subtotal)



# "TION 4
#  A shipping company charges different rates based on weight zones.
# Write a program that asks for a package weight in pounds and converts it to kilograms
#  (1 pound = 0.453592 kg). 
# Then calculate the shipping cost: $5.00 for packages under 2 kg, $8.50 for packages 2-5 kg,
# # and $12.00 for packages over 5 kg."


# p_weight= int(input("Enter package weight in pounds: "))
# weight = round(p_weight*0.453592)

# if weight < 2:
#        print("Shipping Cost = $5.00")
# elif weight >= 2 and weight < 5: 
#        print("Shipping Cost = $8.50")
# else:
#        print("Shipping Cost = $12.00")


# . Create a program that asks a user for their age, 
# weight in pounds, and height in inches. Calculate
# and display their BMI using the formula: BMI = 703 × weight ÷ (height × height). 
# # Also calculate their target heart rate zone (220 - age)
# # × 0.7 for the lower bound and (220 - age) × 0.85 for the upper bound

#  A library system needs to process book checkouts.
# Write a program that asks for the patron's name, book title, 
#  and checkout period in days. Display a receipt showing:
#  "Patron: [name]", "Book: [title]", "Due in: [days] days", and "Late fee per day: $0.25".


# name = str(input("Enter patron name: "))
# book = str(input("Enter book title:"))
# checkout = int(input("Enter check out period:"))

# print(f"Patron: {name} ",f"Book: {book}", f"Due in: {checkout} days", "Late fee per day: $0.25")

#. A teacher wants to take attendance for 25 students.
#  Write a program that asks the teacher to enter a student number (1-25) for each student present
# . For each entry, print "Student [number] is present.
# " Use a for loop to handle exactly 25 attendance entries.



# for x in range(1,25):
#        stdnum = int(input("Enter a student number:"))
#        print(f"Student {stdnum} is present")
       
       

# A concert venue has 150 seats numbered 1 through 150.
# Write a program that prints all available seat numbers in this format:
#  "Seat 1, Seat 2, Seat 3..." all on the same line, separated by commas. 
# ask the user how maneats (starting from seat 1) should be marked as unavailable.

# for x in range(1,151):
#     venue = (print(f"Seat {x}" , end=" , "))

# A meteorologist needs to log temperatures for a week.
#  Write a program using a for loop that asks the user to 
# enter the temperature for each day of the week (Day 1 through Day 7).
#  After each temperature is entered,
#  calculate and print whether it's above or below the average temperature of 72°F.

# for x in range(1,8):
#         temperature = int(input("Enter the tempreature:"))
#         if temperature > 72:
#                 print("Tempreature is above average")
#         else:
#                 print("Tempreature is below average")



# A teacher needs to calculate letter grades for test scores.
#  Write a program that uses a for loop to ask for 10 test scores.
#  For each score, immediately print the letter 
# grade: A (90-100), B (80-89), C (70-79), D (60-69), or F (below 60).
# After all scores are entered, print "Grade calculation complete."


# for x in range(1,10):
#         score = int(input("Enter a test score:"))
#         if score >=90 and score<=100:
#                 print("grade = A")
#         elif score >=80 and score <= 89:
#                 print("grade = B")
#         elif score >= 70 and score<=79:
#                 print("grade = C")
#         elif score >=60 and score<= 69:
#                 print("grade = D")
#         elif score < 60:
#                 print("grade = F")


#  A store manager wants to count inventory across 
# multiple product categories. Write a program that uses for loops to print
#        the following pattern, representing different product codes:
# "A1, A2, A3, ..., A10" for Electronics, then "B1, B2, B3, ..., B15"
#        for Clothing, then "C1, C2, C3, ..., C5" for Books. Print each category on a separate line.
        


num = int(input("enter a number:"))
sum = 0

while num > 0:
        sum += num
        num = int(input("enter a number:"))

print(sum)