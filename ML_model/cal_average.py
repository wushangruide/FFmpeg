import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xlrd
import xlwt
from xlutils.copy import copy

per_b768_r20_s720_r30_r40 = []
per_b768_r20_s720_s1280_s1920 = []
per_b768_r20_s720_b1024_b1536 = []
per_b768_r20_s720 = []
#workbook1 = xlrd.open_workbook("combi.xls", formatting_info=True)
workbook = xlrd.open_workbook("combi.xls")
#nrows=worksheet.nrows
newWB = copy(workbook)
worksheet_2combi = workbook.sheet_by_name("2")
worksheet_3combi = workbook.sheet_by_name("3")
worksheet_4_2combi = workbook.sheet_by_name("4_2")
worksheet_5combi = workbook.sheet_by_name("5")
worksheet_r20 = workbook.sheet_by_name("r20")
worksheet_r30 = workbook.sheet_by_name("r30")
worksheet_r40 = workbook.sheet_by_name("r40")
worksheet_b768 = workbook.sheet_by_name("b768")
worksheet_b1024 = workbook.sheet_by_name("b1024")
worksheet_b1536 = workbook.sheet_by_name("b1536")
worksheet_720_480 = workbook.sheet_by_name("720-480")
worksheet_1280_800 = workbook.sheet_by_name("1280-800")
worksheet_1920_1080 = workbook.sheet_by_name("1920-1080")

time_3combi = worksheet_3combi.col_values(2,0,6000)
time_r20 = worksheet_r20.col_values(1,0,2000)
time_r30 = worksheet_r30.col_values(1,0,2000)
time_r40 = worksheet_r40.col_values(1,0,2000)
time_b768 = worksheet_b768.col_values(1,0,2000)
time_b1024 = worksheet_b1024.col_values(1,0,2000)
time_b1536 = worksheet_b1536.col_values(1,0,2000)
time_720_480 = worksheet_720_480.col_values(1,0,2000)
time_1280_800 = worksheet_1280_800.col_values(1,0,2000)
time_1920_1080 = worksheet_1920_1080.col_values(1,0,2000)

a = 0
b = 0
c = 0

for i in range(2000):
    per_b768_r20_s720.append((time_b768[i] + time_r20[i] + time_720_480[i] - time_3combi[i])/(time_b768[i] + time_r20[i] + time_720_480[i]))

for j in range(2000):
    newWS = newWB.get_sheet(1)
    newWS.write(j, 5, per_b768_r20_s720[j])
newWB.save("combi.xls")
'''
for i in range(6000):
    if (i+1) % 3 == 1:
        per_b768_r20_s720_r30_r40.append((time_b768[a] + time_r20[a] + time_720_480[a] + time_r30[a] + time_r40[a]- time_5combi[i]) / (time_b768[a] + time_r20[a] + time_720_480[a] + time_r30[a]+ time_r40[a]))
        a += 1
    elif (i+1) % 3 == 2:
        per_b768_r20_s720_s1280_s1920.append((time_b768[b] + time_720_480[b] + time_r20[b] + time_1280_800[b] + time_1920_1080[b] - time_5combi[i]) / (time_b768[b] + time_720_480[b] + time_r20[b] + time_1280_800[b] + time_1920_1080[b]))
        b += 1
    else:
        per_b768_r20_s720_b1024_b1536.append((time_r20[c] + time_720_480[c] + time_b768[c] + time_b1024[c] + time_b1536[c]- time_5combi[i]) / (time_r20[c] + time_720_480[c] + time_b768[c] + time_b1024[c] + time_b1536[c]))
        c += 1
print(per_b768_r20_s720_r30_r40)


for j in range(2000):
    newWS = newWB.get_sheet(4)
    newWS.write(3*j, 5, per_b768_r20_s720_r30_r40[j])
    newWS.write(3*j+1,5,per_b768_r20_s720_s1280_s1920[j])
    newWS.write(3*j+2,5,per_b768_r20_s720_b1024_b1536[j])
newWB.save("combi.xls")
'''


