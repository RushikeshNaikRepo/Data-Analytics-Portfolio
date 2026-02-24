print("Hello World")

############

First_name = "Tony"
Last_name = "Stark"
Age = 51
About = "Tony is a genius"
print("Hello There! My name is", First_name, Last_name, "& my age is", Age)
print("Hello Tony. Nice to meet you. We often hear from people that", About)

############

old_age = int(input("Enter your old age:"))
new_age = old_age + 4
print(new_age)

############

First = int(input("Enter your first number:"))
Second = int(input("Enter your second number:"))
sum = First + Second
print(sum)

############

name = "Tony Stark"
print(name)
print(name.upper())
print(name.lower())
print(name.find("S"))
print(name.find("U"))

############

name = "Tony Stark"
print(name)
print(name.replace("Tony Stark", "Iron Man"))

############

name = "Robert Downey"
print("S" in name)
print("R" in name)

############

print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 // 2)
print(5 % 2)
print(5 ** 2)

############

i = 5
i = i + 2
i += 2
i -= 2
i *= 2
i /= 2

############

print(2 > 3 or 2 > 1)
print(2 > 3 or 2 > 4)
print(2 < 3 or 2 > 1)
print(2 < 3 or 2 > 4)

print(3 > 2 and 2 > 1)
print(3 > 2 and 2 > 4)
print(3 < 2 and 2 > 1)
print(3 < 2 and 2 > 4)

print(not 2 > 3)
print(not 2 > 4)
print(not 3 > 2)
print(not 3 > 4)

############

age = 2

if age >= 18:
    print("You are old enough to vote")
    print("You are and Adult")
elif age < 18 and age > 3:
    print("You are in school")
else:
    print("You are a child")

print("Thank You")

############

First_Number = int(input("Enter your first number:"))
Operator =  input("Enter your operator ( +, -, *, /. =):")
Second_Number = int(input("Enter your second number:"))

if Operator == "+":
    print(First_Number + Second_Number)
    if Operator == "-":
        print(First_Number - Second_Number)
        if Operator == "*":
            print(First_Number * Second_Number)
            if Operator == "/":
                print(First_Number / Second_Number)
                if Operator == "*":
                    print(First_Number * Second_Number)
else:
    print("Invalid operator")

############

i = 1

while i <= 10:
    print(i)
    i += 1

i = 5
while i >+ 0:
    print(i * "*")
    i = i - 1

############

marks = [95, 98, 97, "Maths"]
print(marks)
print(marks[1])
print(marks[3])
print(marks[-1])
print(marks[0:2])
print(marks[:2])
print(marks[1:3])

marks = [95, 98, 97]
for score in marks:
    print(score)

marks = [95, 98, 97]
marks.append(96)
marks.insert(0, 99)
print(marks)

print(99 in marks)
print(93 in marks)
print(len(marks))

marks = [95, 98, 97]
i = 0
while i < len(marks):
    print(marks[i])
    i += 1

############

students = ["ram", "shyam", "kishan", "radha", "radhika"]

for student in students:
    if student == "radha":
        break;
    print(student)

############

marks = (95, 98, 97, 97, 97)
print(marks.count(95))
print(marks.index(97))
print(marks.count(97))

############

marks = {"englissh" : 90, "Chemistry" : 98, "Physics" : 95}
print(marks["Physics"])

############

import math
print(dir(math))

from math import sqrt
print(sqrt(4))
print(sqrt(16))

def print_sum(first, second):
    print(first + second)
print_sum(1, 2)