# -*- coding: utf-8 -*-
import pandas as pd

s = pd.Series([1,2,3], index=['a','b','c']) #创建一个序列s
d = pd.DataFrame([[1,2,3],[4,5,6]], columns=(['a','b','c'])) #创建一个表
d2 = pd.DataFrame(s) #也可以用已有的序列来创建表格

d.head() #预览前5行数据
d.describe() #数据基本统计量

print(d)
print(d2)

#读取文件，注意文件的存储路径不能带有中文，否则读取可能出错
pd.read_excel('data.xls')
pd.read_csv('data.csv', encoding = 'utf-8') #读取文本格式的数据，一般用encoding指定编码