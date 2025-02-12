import os

import openpyxl

merge_file = open("merge.txt","r",encoding="ANSI")
lines = merge_file.readlines()

"""  
for index,row in enumerate(lines):
    print("index:"+str(index),"row:"+row)
    locals()["workbook"+str(index)] = openpyxl.load_workbook(row.split(",")[0],data_only=True)
    print(locals()["workbook"+str(index)].sheetnames)
    locals()["worksheet"+str(index)] = locals()["workbook"+str(index)].active
    print(locals()["worksheet"+str(index)].title)
"""

for i in range(1,len(lines)):
    locals()["workbook"+str(i)] = openpyxl.load_workbook(lines[i].split(",")[0],data_only=True)
    print(locals()["workbook"+str(i)].sheetnames)
    locals()["worksheet"+str(i)] = locals()["workbook"+str(i)].active
    print(locals()["worksheet"+str(i)].title)


for i in range(2,len(lines)):
    print(i)
    for row in locals()["worksheet"+str(i)].iter_rows(min_row=int(lines[i].split(",")[1])):
        print(row)
        row_values = [cell.value for cell in row]
        locals()["worksheet1"].append(row_values)


locals()["workbook1"].save(lines[0].split(",")[0])




merge_file.close()


