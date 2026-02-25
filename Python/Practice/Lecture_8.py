# OOP - Object Oriented Programming.

# class Student:
#     name = "Rushikesh Naik"
# s1 = Student()
# print(s1)



# Contructor -- __init__ Function
# class Student:
#     name = "Ruhsi"
#     def __init__(self):
#         print("adding new student in database..")
# s1 = Student()



# class Student:
#     college_name = "ABC College"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marls = marks 

#     def welcome(self):
#         print("Welcome Student")

# s1 = Student("Karan", 97)
# s1.welcome()

#PRactice Question
#Question - Create student class that takes name & marks of 3 subjects as arguments in constructor.
#Then create a method to print the avergage.
#ANSWER -- 
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0 
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "Your avg score is", sum/3)

# s1 = Student("tone stark", [99, 98, 97])
# s1.get_avg()



# Static Methods
# Abstraction
# Encapsulation