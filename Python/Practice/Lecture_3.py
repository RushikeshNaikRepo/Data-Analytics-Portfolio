## LIST AND TUPELS ##
# marks = [94.4, 87.5, 95.2, 66.4, 45.1]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[3])

# student = ["karan", 95.4, 17, "Delhi"]
# print(student)

### IMPORTANT NOTES -- 
## STRINGS are immutable in python. Cannot Change.
## LISTS are mutable in python. Can change.
## TUPELS are immutable. cannot change.

# # marks = [85, 94, 76, 63, 48]
# # print(marks)
# # print(marks[1:4])
# # print(marks[:4])
# # print(marks[1:])
# # print(marks[-3:-1])

# #LIST MERTHODS 

# list = [2, 1, 3]
# print(list)

# #append method
# list.append(4)
# print(list)

# #sort method (asc)
# list.sort()
# print(list)

# #sort reverse (desc) method
# list.sort(reverse= True)
# print(list)

# list1 = ["banana", "litchi", "apple"]
# print(list1)

# list1.sort(reverse = True)
# print(list1)

# list1.sort()
# print(list1)

# list2 = ["a", "d", "e", "f", "c", "b"]
# print(list2)

# #reverse method
# list2.reverse()
# print(list2)

# #insert method
# list2.insert(1,"u")
# print(list2)

#remove method
# list3 = [2, 1, 3, 1]
# print(list3)
# list3.pop(2)
# print(list3)


## TUPLES 
# tup = (2, 1, 3, 1)
# print(type(tup))
# print(tup[0])
# print(tup[1])

# tup = ()
# print(tup)
# print(type(tup))

# tup = (1)
# print(tup)
# print(type(tup))

# tup = (1 ,2 ,3, 4)
# print(tup[1:3])

## TUPLE METHODS 

#INDEX METHOD
# tup = (1, 2, 3, 4, 2, 2)
# print(tup.index(2))

# print(tup.count(2))


#PRACTICE QUESTION 
#QUESTION 1 -- WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
##ASNWER 1 - 
# a = input("first movie: ")
# b = input("second movie: ")
# c = input("third movie: ")
# print("[",a,",",b,",",c,",","]")

##ASNWER 2 - 
# movies = []
# movies.append(input("First Movie: "))
# movies.append(input("Second Movie: "))
# movies.append(input("Third Movie: "))
# print(movies)

#QUESTION 2 -- WAP to check if a list contains a palindrome of elements. (Hint: use copy() method).
# #ANSWER - 
# list1 = ["m", "a", "a", "m", "g"]
# copy_list1 = list1.copy()
# copy_list1.reverse()
# if(copy_list1 == list1):
#     print("Palendrome")
# else:
#     print("Not Palendrome")

#QUESTION3 -- WAP to count the number of students with "A" grae in the following tuple - 
# ##["C", "D", "A", "A", "B", "B" "A"]
# #ANSWER - 
# grade = ("C", "D", "A", "A", "B", "B", "A")
# print(grade.count("A"))

#QUESTION 4 - Store the below values in a list and sort them from "A" to "D"
##"C", "D", "A", "A", "B", "B", "A"
#ANSWER -
# grade = ["C", "D", "A", "A", "B", "B", "A"]
# grade.sort()
# print(grade)