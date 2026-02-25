# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass


# acc1 = Account("12345", "abcde")

# print(acc1.acc_no)
# print(acc1.acc_pass)



# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

# acc1 = Account("12345", "abcde")

# print(acc1.acc_no)
# print(acc1.__acc_pass)

#Polymorphism : Operator Overloading.

# class Complex:
#     def __init__(self, real, img):
#         self.real = real 
#         self.img = img 

#     def ShowNumber(self):
#         print(self.real, "i +", self.img, "j")

# num1 = Complex(1, 3)
# num1.ShowNumber()