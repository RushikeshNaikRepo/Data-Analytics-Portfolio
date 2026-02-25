# #Functions
# a = 5
# b = 10

# sum = a + b
# print(sum)

# def calc_sum(a, b):
#     sum = a + b
#     print(sum)

# calc_sum(5, 10)
# calc_sum(2, 10)
# calc_sum(12, 17)


# def calc_sum(a, b):
#     return a + b

# sum = calc_sum(1, 2)
# print(sum)

# sum = calc_sum(178, 2221)
# print(sum)

#average of 3 numbers

# def calc_avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg

# calc_avg(98, 97, 95)

# print("rushikesh", "naik")

# print("rushilesh", end=" ")
# print("naik")

#Practice Question - 

#Q1 - WAF to print the length of a list. (list is a parameter).
# cities = ["delhi", "gurgoan", "noida", "pune", "mumbai", "chennai", "kolakta"]
# heroes = ["Iron man", "thor", "captain america", "shaktiman"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)

#Q2 - WAF to print the elements of a list in a single line. (list is the parameter).
# cities = ["delhi", "gurgoan", "noida", "pune", "mumbai", "chennai", "kolakta"]
# heroes = ["Iron man", "thor", "captain america", "shaktiman"]

# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(cities)
# print_list(heroes)

#Q3 - WAF to find the factorial of n. (n is the parameter).

# def calc_fact(n):
#     fact = 1 
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# calc_fact(6)

#Q4 - WAF to convert USD to INR.
# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "usd =", inr_val, "INR")

# converter(73)


## Recursion ##
# def show(n):
#     if (n ==0):
#         return
#     print(n)
#     show(n-1)
# show(3)


# def fact(n):
#     if ( n == 0 or n == 1):
#         return 1
#     return fact(n - 1) * n
# print(fact(6))

#PRACTICE QUESTION:
#QUESTION1 - Write a recursive function to calculate the sum of firt n natural numbers.
# def calc_sum(n):
#     if(n == 0):
#        return 0
#     return calc_sum(n-1) + n

# sum = calc_sum(20)
# print(sum)

#QUESTION2 - Write a recursive function to print all elements in a list.  Hint - use list and index as parameters.
# def print_list(list, idx =0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx +1)

# fruits = ["mango", "litchi", "apple", "banana"]
# print_list(fruits)