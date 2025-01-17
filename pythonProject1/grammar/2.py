import os

from module import *
from pythonProject1.grammar.module import TestFile

"""
list1 = ['Andy','Robert','Lucas']
for index, value in enumerate(list1):
    print(index, value)
"""

"""
set1 = {1,1,1,2,3,4,4,3,2}
for i in set1:
    print(i)
"""

"""   
input1 = input("请输入选项.e:退出.c:继续")
if input1 == "e":
    print("退出")
elif input1 == "c":
    print("继续")
else:
    print("请输入正确选项")
"""

# print(TestFile.get_file_name(os.getcwd(),"1"))

str1 = """
Hello
Andy
"""
print(str1)

str2 = ("Hello"
        "Andy")
print(str2)

print(f"QQQQ{str1}")  #f格式化字符串

#print('C:\some\name')
print(r'C:\some\name') #r取消\的转义作用


list1 = []
list1.append(1)
list1.append(2)
list1.append(3)
print(len(list1))








