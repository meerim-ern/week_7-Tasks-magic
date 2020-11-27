##1

# class MyList(list):
#     def __getitem__(self,index):
#         if index ==0:
#             raise ValueError
#         index = index - 1
#         return list.__getitem__(self,index)

            
# x = MyList([5,2,7])
# print(x[3])

# from functools import reduce

# class Student(dict):
#     name =''
#     surname = ''
#     course = 0
#     points = dict

#     def __init__(self,name,surname,course):
#         self.name = name
#         self.surname = surname
#         self.course = course

#     def points_(self,points):
#         self.points = points
#         for value in points:
#             a = points.values()
#             self.b = round(reduce(lambda x,y: x+y, a)/len(a))

#         print(f"{self.surname} {self.name}, учится на {self.course} курсе, средний балл - {self.b}.")

#     def sort_(self,other):
#         if self.b > other.b:
#             print(f"Cредний балл у {self.name} самая высокая - {self.b} баллов.")
#         else:
#             print(f"Средний балл у {other.name} самая высокая - {other.b} баллов")

   

# student1 = Student("Асан","Айдарбеков",1)
# student2 = Student("Айжан","Керимова",3) 
# student1.points_({"kyrg":80,"eng":100,"hist":100})
# student2.points_({"kyrg":70,"eng":90,"hist":95})
# Student.sort_(student1,student2)

##3

# import math

# class Complex(object):
#     def __init__(self, real, imaginary):
#         self.n = complex(real, imaginary)
#         self.real = real
#         self.imaginary = imaginary
        
#     def __add__(self,no):
#         res = self.n + no.n
#         return Complex(res.real, res.imag)

#     def __sub__(self, no):
#         res = self.n - no.n
#         return Complex(res.real, res.imag)

#     def __mul__(self, no):
#         res = self.n * no.n
#         return Complex(res.real, res.imag)

#     def __truediv__(self, no):
#         res = self.n / no.n
#         return Complex(res.real, res.imag)

#     def mod(self):
#         res = math.sqrt(self.n.real ** 2 + self.n.imag ** 2)
#         return Complex(res.real, res.imag)

#     def __str__(self):
#         if self.imaginary == 0:
#             result = "%.2f+0.00i" % (self.real)
#         elif self.real == 0:
#             if self.imaginary >= 0:
#                 result = "0.00+%.2fi" % (self.imaginary)
#             else:
#                 result = "0.00-%.2fi" % (abs(self.imaginary))
#         elif self.imaginary > 0:
#             result = "%.2f+%.2fi" % (self.real, self.imaginary)
#         else:
#             result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
#         return result

# if __name__ == '__main__':
#     c = map(float, input().split())
#     d = map(float, input().split())
#     x = Complex(*c)
#     y = Complex(*d)
#     print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')





    




