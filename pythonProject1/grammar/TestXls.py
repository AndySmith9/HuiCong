import xlrd
from xlwt import Workbook

"""
解决问题:
Q1:xlrd如何判断空单元格?
Q2:xlwt如何将单元格置空?
"""

xls_workbook = xlrd.open_workbook("1.xls")
xls_sheet = xls_workbook.sheet_by_name("Sheet1")
print(xls_sheet.nrows)
print(xls_sheet.cell(0,0))
for i in range(0,xls_sheet.nrows):
    if xls_sheet.cell(i,0).value == "":
        print(i+1,xls_sheet.cell(i,0))


write_xls_workbook = Workbook()
write_sheet = write_xls_workbook.add_sheet("Test")
for i in range(0,10):
    if i == 3:
        write_sheet.write(i, 0, "")
    elif i == 8:
        write_sheet.write(i, 0, None)
    else:
        write_sheet.write(i, 0, i)

write_xls_workbook.save("Test.xls")