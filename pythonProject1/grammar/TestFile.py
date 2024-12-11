import os

def get_file_name(folderPath,key):
    for file in os.listdir(folderPath):
        if key in file:
            return file

print(get_file_name("D:\\店铺产品-jishunzen1@163.com\\20241212","库存"))





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
