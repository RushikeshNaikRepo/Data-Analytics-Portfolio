# ## DICTIONARIES AND SET

# #Dictionaries
# # dict = {
# #     "key" : "value",
# #     "name" : "Rushikesh Naik",
# #     "subjects" : ["Python", "c", "Java"],
# #     "topics" : ("dictionary", "sets"),
# #     "age" : 35,
# #     "is_adult" : True,
# #     "marks" : 94.4
# # }
# # print(dict)
# # print(type(dict))

# # print(dict["subjects"])

# # dict["name"] = "Apna College"
# # print(dict)

# # dict["Course name"] = "Data science & analytics"
# # print(dict)

# # null_dict = {}
# # print(null_dict)

# ## Nested Dictionaries

# # Student = {
# #     "name" : "Rahul Kumar",
# #     "Subjects" : {
# #         "Physics" : 95, 
# #         "Chemistry" : 88
# #     }
# # }

# # print(Student["Subjects"]["Physics"])


# # DICTIONARIES METHODS 

# # Keys method
# # Student = {
# #     "name" : "Rahul Kumar",
# #     "Subjects" : {
# #         "Physics" : 95, 
# #         "Chemistry" : 88
# #     }
# # }

# # print(Student.keys())
# # print(len(list(Student.keys())))

# # Values method
# # Student = {
# #     "name" : "Rahul Kumar",
# #     "Subjects" : {
# #         "Physics" : 95, 
# #         "Chemistry" : 88
# #     }
# # }
# # print(Student.values())
# # print(list(Student.values()))

# # .items method
# # Student = {
# #     "name" : "Rahul Kumar",
# #     "Subjects" : {
# #         "Physics" : 95, 
# #         "Chemistry" : 88
# #     }
# # }
# # print(Student.items())
# # print(list(Student.items()))

# # .get method
# # Student = {
# #     "name" : "Rahul Kumar",
# #     "Subjects" : {
# #         "Physics" : 95, 
# #         "Chemistry" : 88
# #     }
# # }

# # print(Student["name"])  #Error if wrong or invalid or absent value.
# # print(Student.get("name")) # No eeor -> None value.

# # update method
# # Student = {
# #     "name" : "Rahul Kumar",
# #     "Subjects" : {
# #         "Physics" : 95, 
# #         "Chemistry" : 88
# #     }
# # }

# # Student.update({"name" : "Neha Kumar"})

# # print(Student)


# ## SETS ##  -- Sets are unorder. ingore dpulicate values.

# ### ***IMPORTANT  -- SETS ARE MUTABLE BUT ELEMTNS WITHIN SETS ARE IMMUTABLE*** ###

# # Collection = {1, 2, 3, 4, "hello", "world", 2, "world"}

# # print(Collection)
# # print(type(Collection))
# # print(len(Collection))

# # Rushi = set()
# # print(type(Rushi))

# ##SET METHODS 
# #Add Method 
# # collection = set()
# # collection.add(1)
# # collection.add(2)
# # print(collection)

# #Remove method
# # collection.remove(2)
# # print(collection)

# #Clear method
# # collection = set()
# # collection.add(1)
# # collection.add(2)
# # collection.add("Rushikesh Naik")
# # collection.add((1, 2, 3))
# # collection.clear()
# # print(collection)
# # print(len(collection))

# #POP Method
# # Collection = {"Hello", "Rushikesh Naik", "World", "Coding", "Python"}
# # print(Collection)
# # print(Collection.pop())
# # print(Collection.pop())

# # union method -- Combines both set values & returns new.
# # set1 = {1, 2, 3}
# # set2 = {2, 3, 4}

# # print(set1.union(set2))
# # print(set1)
# # print(set2)

# #intersection method -- Combines common values & returns new.
# # set1 = {1, 2, 3}
# # set2 = {2, 3, 4}

# # print(set1.intersection(set2))
# # print(set1)
# # print(set2)

# ##Practice Questions 
# ##ANSWER 1 - 
# # dict = {
# #     "cat" : "a small animal",
# #     "table" : ["a piece of furniture", "list of facts & figures"]
# # }

# # print(dict)

# ##ANSWER 2 -
# # subjects = {
# #     "python", "java", "c++", "python", "javascript", "java", 
# #     "python", "java", "c++", "c"
# #     }

# # print(len(subjects))

# ##ANSER 3 - 
# # marks = {}
# # x = int(input("enter physics: "))
# # marks.update({"physics" : x})
# # x = int(input("enter maths: "))
# # marks.update({"maths" : x})
# # x = int(input("enter chem: "))
# # marks.update({"chem:" : x})
# # print(marks)

# ##ANSWER 3.1 - 
# values = {
#     ("float", 9.0),
#     ("int", 9)
# }
# print(values)