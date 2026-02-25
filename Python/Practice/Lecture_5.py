## LOOPS 

# count = 1
# while count <= 5 :
#     print("hello")
#     count += 1
# print(count)

# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# print ("loop ended")

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1
# print ("loop ended")

## WHILE LOOP PRACTICE QUESTION ##
#Q1 - Print numbers from 1 to 100 
# i = 1
# while i <= 100:
#     print(i)
#     i += 1
# print("printed 1 to 100 number")

#Q2 - print numbers from 100 to 1
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1
# print("printed 100 to 1 number")

#Q3 - print the multiplication table of a number n
# n = int(input("Enter N Number: "))
# i = 1
# while i <= 10:
#     print (i * n)
#     i += 1

#Q4 - print the elements of the following list using a loop.
#[1,4,9,16,25,36,49,64,81,100]
#ans1 -
# nums = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx+= 1
#ans 2- 
# heroes = ["iron man", "superman", "thor", "batman", "loki"]
# idx = 0
# while idx < len(heroes):
#     print(heroes[idx])
#     idx+= 1

#Q5 - search for a number X in this tuple using loop.
#[1,4,9,16,25,36,49,64,81,100]
# nums = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("Enter X Number: "))
# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("Found at i", i)
#     else:
#         print("Could Not Found", i)
#     i += 1
# print("End of Loop")

## Break & Continue 
##Break -
# nums = (1,4,9,16,25,36,49,64,81,100,36)
# x = 36
# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("Found at i", i)
#         break
#     else:
#         print("Could Not Found", i)
#     i += 1
# print("End of Loop")

## For Loop 
# nums = [1, 2, 3, 4, 5]
# for val in nums:
#     print(val)

# veggies = ["potato", "brinjal", "ladyfinger", "cucumber"]
# for val in veggies:
#     print(val)

# tup = (1,2,3,4,2,8,9)
# for val in tup:
#     print(val)

# str = "rushikeshnaik"
# for char in str:
#     if (char == 's'):
#         print("s found")
#         break
#     print(char)
# else:
#     print("END")

#PRACTICE QUESTIONS
#Q1 - print the elements of the following list using a loop.
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#Ans - 
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for el in nums:
#     print(el)

#Q2 - search for a number x in this tuple using loop.
#(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
#Ans - 
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
# x = 49

# idx = 0
# for el in nums:
#     if(el == x):
#         print("number found at idx", idx )
#         break
#     idx +=1


## range function 
# for i in range(10):
#     print(i)

# for i in range(2, 10):
#     print(i)

# for i in range(2, 10, 2):
#     print(i)

# PRACTICE QUESTION --

#Q1 - Print numbers from 1 to 100.
# for i in range(1,101):
#     print(i)

#Q2 - print numbers from 100 to 1.
# for i in range(100, 0, -1):
#     print(i)

#Q3 - print the multiplication table of a number n.
# n = int(input("enter number:"))

# for i in range(1, 11):
#     print(n * i)

#Pass Statement.
# for i in range(5):
#     pass
#     #empty
# print("some useful work")

##PRACTICE##

#QUESTION - 1 
# WAP to find the sum of first time n numbers. (using while).
#ANS -- 
#USING WHILE --
# n = 7
# sum = 0
# i = 1
# while i <=n:
#     sum += i
#     i +=1
# print("total sum = ", sum)

#USING FOR -- 
# n = 7
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("total sum = ", sum)

#QUESTION - 2
#WAP to find the factorial of first n numbers. (using for).
#ANS -- 
#USING WHILE --
# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1

# print("Factorial is", fact)

# USING FOR -
# n = 5
# fact = 1
# i = 1
# for i in range(1, n+1):
#     fact *= i
#     i += 1
# print("Factorial is", fact)