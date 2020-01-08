import os
import re
import xlwt

file_name = '_file_format'
file = []
filename = [] #ffmpeg use this keyword, just for keep the same with ffmpeg file
duration = []
size = []
bit_rate = []


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

def content_search(path, keyword1, keyword2, keyword3, keyword4):
    with open(path,'r') as file:
        for line in file:
            if keyword1 in line:
                #temp1 = line.rsplit('=')
                print(line)
                filename.append(line)
            if keyword2 in line:
                temp2 = line.rsplit('=')
                duration.append(line)
            if keyword3 in line:
                temp3 = line.rsplit('=')
                size.append(line)
            if keyword4 in line:
                temp4 = line.rsplit('=')
                bit_rate.append(line)
            '''
            if keyword5 in line:
                temp5 = line.rsplit(None)
                operation.append(temp5[1:])
            '''
search(os.getcwd(), file_name)
print(file)
workbook = xlwt.Workbook()


#file_table = path.rsplit("/")
sheet = workbook.add_sheet("1")
sheet.write(0, 0, 'filename')
# sheet.write(0, 1, 'operation')
sheet.write(0, 1, 'duration')
sheet.write(0, 2, 'size')
sheet.write(0, 3, 'bite_rate')
i = 1
for path in file:
    filename = []
    #operation = []
    duration = []
    size = []
    bit_rate = []
    #content_search(path, 'real', 'user', 'sys', 'input', 'operation')

    #print(len(time_user),len(time_real),len(time_sys))
    content_search(path, 'filename=', 'duration=', 'size=', 'bit_rate=')
    cou = len(filename)

    #reset following parameters
    for co in range(cou):
        #name = re.findall(r"\d+",path)
        #str = "".join(name)
        #sheet.write(0, i, str)
        a = len(filename)
        b = len(duration)
        if a == b:
            None
        else:
            print(path)
        sheet.write(i, 0, filename[co])
        #print(input_name,co)
        #sheet.write(i, 1, operation[co])
        #try:
        sheet.write(i, 1, duration[co])
        sheet.write(i, 2, size[co])
        sheet.write(i, 3, bit_rate[co])
        #except IOError:
        #    print("worry happen in:" + path)
        #else:
        #    print("success")
        i = i + 1
workbook.save(f'{file_name}.xls')
'''

'''