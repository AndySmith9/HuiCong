import os

def get_file_name(folderPath,key):
    for file in os.listdir(folderPath):
        if file.startswith(key):
        # if key in file:
            return file

# print(get_file_name("D:\\店铺产品-jishunzen1@163.com\\20241212","库存"))
"""   
path1 = input("请输入路径:")
key1 = input("请输入文件名关键字:")
print(get_file_name(path1, key1))
"""
print(os.getcwd())
print(get_file_name(os.getcwd(),"xls"))


"""  
readFile = open("test.txt","r")
lines = readFile.readlines()
for line in lines:
    print(line.split()[0])
    print(type(line.split()[0]))
"""




"""   
readFile = open("input.txt","r",encoding="UTF-8")
lines = readFile.readlines()
for line in lines:
    if "#" not in line:
        print(line)
        print(line.split(",")[0])
        print(line.split(",")[1])


filePath = "D:\\店铺产品-jishunzen1@163.com\\20241212"

for absolutePath,directories,files in os.walk(filePath):
    print(absolutePath)
    print(directories)
    print(files)

print(os.listdir(filePath))
for file in os.listdir(filePath):
    if "库存" in file:
        print(file)
"""
