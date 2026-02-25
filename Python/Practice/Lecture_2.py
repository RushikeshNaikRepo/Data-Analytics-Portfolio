# str1 = "This is a string.\tWe are creating it in python."
# print (str1)

# Concatenation -- 
# str1 = "Rushikesh"
# str2 = "Naik"
# final_str = str1+str2
# print(final_str)

#Length -- 
# str1 ="Rushi"
# len1 = len(str1)
# print(len1)

# str2 = "Naik"
# len2 = len(str2)
# print(len2)

# final_str = str1 + " " + str2
# print(len(final_str))


#Slicing 
#R u s h i k e s h
#0 1 2 3 4 5 6 7 8
# str = "Rushikesh_Naik"
# print(str[10:14])
# print(str[:9])
# print(str[10:])

# #slicing with negative index 
# # A  p  p  l  e 
# #-5 -4 -3 -2 -1
# str = "apple"
# print(str[-3:-1])
# print(str[-5:-2])

#STRING FUNCTIONS 
#end swith 
# str = "I am studying python from apna college"
# print(str.endswith("app"))

#capitalized
# str = "i am studying python from apna college"
# print(str.capitalize()) #Creates a new string with changes. does not make changes to existing string
# print(str)

#Replace
# str = "i am studying python from apna college"
# print(str.replace("python","java script"))

#find
# str = "i am studying python from apna college"
# print(str.find("o"))

#count 
# str = "i am studying python from apna college"
# print(str.count("o"))


#Practice Questions = 
#Question 1 - WAP to enter first name and print its length
# first_name = input("Enter Your First Name: ")
# print(len(first_name))

#Question2 - WAP to find the occurence of '$' in a string.
# str = "Hi, I am the $ symbol $99.99"
# print(str.count("$"))

#CONDITIONAL STATEMENTS
# SYNTAX = if-elif-else

# age = 24
# if(age>=18):
#     print("can vote")
#     print("can drive")

# light = "green"
# if(light == "red"):
#     print("stop")
# elif(light =="green"):
#      print("go")
# elif(light == "yellow"):
#      print("wait")

# light = "yellow"
# if(light == "red"):
#     print("stop")
# elif(light =="green"):
#      print("go")
# elif(light == "yellow"):
#      print("wait")
# else:
#      print("light is broken")

# age = 16
# if(age>=18):
#      print("can vote") # intendation
# else:
#     print("cannot vote")

#Grade students based on marks.
# marks = int(input("please enter student marks: "))
# if(marks >= 90):
#     grade = 'A'
# elif(marks>= 80):
#     grade = "B"
# elif(marks >= 70):
#     grade = "C"
# else:
#     grade = "D"
# print("grade of the sutend =", grade)


#NESTING - A statement within a statement.
# age = 50
# if (age >=18):
#     if(age >= 80):
#         print("cannot drive")
#     else:
#         print("can dive")
# else:
#     print("cannot drive")

# PRACTICE QUESTIONS
#QUESTION 1 -- WAP to check if a number entered by the user is odd or even.
##ANSWER -- 
# num = int(input("enter Number: "))
# if(num % 2 == 0):
#     print("EVEN NUMBER")
# else:
#     print("ODD NUMBER")

#QUESTION 2 -- WAP to find the greatest of 3 numbers entered by the user.
# a = int(input("enter first number:"))
# b =int(input("enter second number:"))
# c =int(input("enter third number:"))
# if (a>b and a>c):
#     print("first number is largest", a)
# elif (b>c):
#     print("second number is largest", b)
# else:
#     print("third number is largest", c)

#QUESTION3 -- WAP to check if a number is a multiple of 7 or not.
# x = int(input("enter number: "))
# if(x % 7 == 0):
#     print("Multiple of 7")
# else:
#     print("Not a Multiple of 7")