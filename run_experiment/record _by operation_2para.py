import os
import re
import xlwt

file_name = '_rscm'
file = []
input_name = []
operation1 = []
operation2 = []
time_real = []
time_user = []
time_sys = []
para_matrix = []
resolution=["-s 352*288", "-s 680*320", "-s 720*480"]
bitrate=["-r 10", "-r 15", "-r 20"]
codec=["-c:v libx265", "-c:v mpeg4", "-c:v libvpx-vp9"]
operation_co = resolution + bitrate + codec
print(operation_co)

#Listing the file name with a keyword in the documents, every time change the configuration filename, adjusting the function keyword
def search(path, keyword):
    content = os.listdir(path)
    for each in content:
        each_path = path + os.sep + each
        if keyword in each:
            #print(each_path)
            file.append(each_path)
            if os.path.isdir(each_path):
                search(each_path, keyword)

#search(os.getcwd(), 'sm')
#print(file)

def content_search(path, keyword1, keyword2, keyword3, keyword4, keyword5, keyword6):
    with open(path,'r') as file:
        for line in file:
            if keyword1 in line:
                temp1 = line.rsplit(None)
                time_real.append(temp1[1])
            if keyword2 in line:
                temp2 = line.rsplit(None)
                time_user.append(temp2[1])
            if keyword3 in line:
                temp3 = line.rsplit(None)
                time_sys.append(temp3[1])
            if keyword4 in line:
                temp4 = line.rsplit(None)
                input_name.append(temp4[1])
            if keyword5 in line:
                temp5 = line.rsplit(None)
                operation1.append(temp5[1:])
            if keyword6 in line:
                temp6 = line.rsplit(None)
                operation2.append(temp6[1:])
search(os.getcwd(), file_name)
print(file)
workbook = xlwt.Workbook()

#ALL possibility of combinations of two parameters
for i in range(len(operation_co)):
    for k in range(i+1, len(operation_co)):
        para_matrix.append(operation_co[i] +'/'+ operation_co[k])
print(para_matrix)

num = 0
for fi in para_matrix:
    sep_fi = fi.rsplit("/")
    sheet = workbook.add_sheet(f'{num}')
    num = num + 1
    sheet.write(0, 0, 'input')
    sheet.write(0, 1, 'operation1')
    sheet.write(0, 2, 'operation2')
    sheet.write(0, 3, 'real time')
    sheet.write(0, 4, 'user time')
    sheet.write(0, 5, 'sys time')
    i = 1
    for path in file:
        content_search(path, 'real', 'user', 'sys', 'input', 'operation1', 'operation2')
        cou = len(input_name)
        for co in range(cou):
            if ' '.join(operation1[co]) == sep_fi[0] and ' '.join(operation2[co]) == sep_fi[1]:
                sheet.write(i, 0, input_name[co])
                sheet.write(i, 1, operation1[co])
                sheet.write(i, 2, operation2[co])
                sheet.write(i, 3, time_real[co])
                sheet.write(i, 4, time_user[co])
                sheet.write(i, 5, time_sys[co])
                i = i + 1
        input_name = []
        operation1 = []
        operation2 = []
        time_real = []
        time_user = []
        time_sys = []
workbook.save(f'{file_name}.xls')
'''
for path in file:
    content_search(path, 'real', 'user', 'sys', 'input', 'operation1', 'operation2')
    #print(len(time_user),len(time_real),len(time_sys))
    file_table = path.rsplit("/")
    for fi in para_matrix:
        i = 1
        sep_fi = fi.rsplit("/")
        print(sep_fi[0], sep_fi[1])
        sheet = workbook.add_sheet(f'{num}')
        num = num + 1
        cou = len(input_name)
        sheet.write(0, 0, 'input')
        sheet.write(0, 1, 'operation1')
        sheet.write(0, 2, 'operation2')
        sheet.write(0, 3, 'real time')
        sheet.write(0, 4, 'user time')
        sheet.write(0, 5, 'sys time')
        #reset following parameters
        for co in range(cou):
            #print(sep_fi[0],sep_fi[1])
            if operation1[co] == sep_fi[0] and operation2 == sep_fi[1]:
                sheet.write(i, 0, input_name[co])
                #print(input_name,co)
                sheet.write(i, 1, operation1[co])
                sheet.write(i, 2, operation2[co])
                #try:
                sheet.write(i, 3, time_real[co])
                sheet.write(i, 4, time_user[co])
                sheet.write(i, 5, time_sys[co])
                #except IOError:
                #    print("worry happen in:" + path)
                #else:
                #    print("success")
                i = i + 1
        input_name = []
        operation1 = []
        operation2 = []
        time_real = []
        time_user = []
        time_sys = []
workbook.save(f'{file_name}.xls')
'''
