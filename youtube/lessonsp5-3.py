from lessonsp5 import *
import openpyxl as px
book = px.Workbook()
ws = book.active

ws.title = 'No.1'
for i in range(0,len(list)):
     s = 'A' + str(i+2)
     ws[s] = list[i]

book.save('sample.xlsx')
