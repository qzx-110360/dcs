# python 操作excel文档
# 需要先安装 xlrd
# 进入 cmd
# 使用 pip install xlrd  或 python -m install xlrd
import xlrd
# 创建一个打开Excel文档的对象
book=xlrd.open_workbook(r'C:\Users\admin\PycharmProjects\duoceshi\lesson\xlrd.xls')
sheet=book.sheet_by_name('Sheet1') #通过名字选择sheet页面
# sheet.cell_value(2,1)  #通过索引位拿指定的内容
# sheet.row_values(1,0)  #读取指定行，指定范围列中的值
# c=sheet.nrows   #获取当前文件有效的行

# 将Excel文件中的所有内容都读出来，加入到一个列表中，并且一行的内容当作一个元素
# def get_value(col=0):
#     list=[]
#     c=sheet.nrows
#     for i in range(c):
#         a=sheet.row_values(i,col)
#         list.append(a)
#     print(list)
#
# get_value(0)


a=b=[4,5]
c=[4,5]
print(a==b)
print(a is b)
print(a is c)
print(id(a))
print(id(b))
print(id(c))