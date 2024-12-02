"""
Error1:
TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union
"""
int1 = 1
float1 = 1.1
complex1 = 1 + 2j
str1 = """
Hello 
Andy
"""
bool1 = 7 > 6
bool2 = 7 < 6
tuple1 = ()
list1 = []
set1 = set()
dict1 = {}


print(isinstance(int1,int))
print(isinstance(complex1,complex))
print(isinstance(tuple1,tuple))
print(isinstance(tuple1,type(tuple)))
