## File I/O (Input/Output)

# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt", "r")
# line1 = f.readline()
# print(line1)
# f.close()

# f = open("demo.txt", "r")
# line2 = f.readline()
# print(line2)
# f.close()

# f = open("demo.txt", "a")
# f.write("\nafter that powerbi")

# f = open("sample2.txt", "a")
# f.close()

# f = open("demo.txt", "r+")
# f.write("abc")
# print(f.read())

# f = open("demo.txt", "w+")
# print(f.read())
# f.write("abc")

# f = open("demo.txt", "a+")
# print(f.read())
# f.write("abc")

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt", "w") as f:
#     data = f.write("new data")
#     print(data)


#PRACTICE QUESTION -- 
#Q1 - Create a new file "practice.txt" using python, Add the following data in it.
#ANS - 
# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning file I/O\n")
#     f.write("using java.\nI like programming in java.")

#Q2 - WAF that replaces all occurance of "java" with "python" in  above file.
#ANS -- 
# with open("practice.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("java", "python")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)

#Q3 - search if the word "learning exists in the file or not".
# word = "learning"
# with open("practice.txt", "r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("not found")

#Q4 - WAF to find in which line of the file does the word "learning" occue fitst. print-1 if word not found.
#ANS -
# def check_for_line():
#     word = "why"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# print(check_for_line())

#Q5 - from a file containing numbers separated by comma, print the count of even numbers.
#ANS - 
# count = 0
# with open("practice.txt","r") as f:
#     data = f.read()
#     nums = data.split(",")
#     for val in nums:
#         if(int(val) % 2 == 0):
#             count += 1
# print(count)