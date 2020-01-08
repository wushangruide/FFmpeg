import os
import re
import xlwt

file_name = '_file_stream'
file = []
filename = [] #ffmpeg use this keyword, just for keep the same with ffmpeg file
codec_name = []
width = []
height = []
r_frame_rate = []

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

def content_search(path, keyword1, keyword2, keyword3, keyword4,keyword5):
    with open(path,'r') as file:
        for line in file:
            if keyword1 in line:
                #temp1 = line.rsplit('=')
                print(line)
                filename.append(line)
            if keyword2 in line:
                temp2 = line.rsplit('=')
                codec_name.append(line)
            if keyword3 in line:
                temp3 = line.rsplit('=')
                width.append(line)
            if keyword4 in line:
                temp4 = line.rsplit('=')
                height.append(line)
            if keyword5 in line:
                temp5 = line.rsplit(None)
                r_frame_rate.append(line)
search(os.getcwd(), file_name)
print(file)
workbook = xlwt.Workbook()


#file_table = path.rsplit("/")
sheet = workbook.add_sheet("1")
sheet.write(0, 0, 'filename')
# sheet.write(0, 1, 'operation')
sheet.write(0, 1, 'codec_name')
sheet.write(0, 2, 'width')
sheet.write(0, 3, 'height')
sheet.write(0, 4, 'r_frame_rate')
i = 1
for path in file:
    filename = []
    #operation = []
    codec_name = []
    width = []
    height = []
    r_frame_rate = []
    #content_search(path, 'real', 'user', 'sys', 'input', 'operation')

    #print(len(time_user),len(time_real),len(time_sys))
    content_search(path, 'Input #0, mpegts, from', 'codec_name=', 'width=', 'height=', 'r_frame_rate')
    cou = len(filename)

    #reset following parameters
    for co in range(cou-1):
        #name = re.findall(r"\d+",path)
        #str = "".join(name)
        #sheet.write(0, i, str)
        a = len(filename)
        b = len(codec_name)
        if a == b:
            None
        else:
            print(path)
        sheet.write(i, 0, filename[co])
        #print(input_name,co)
        #sheet.write(i, 1, operation[co])
        #try:
        if co % 2 != 0:
            co = co + 1
        sheet.write(i, 1, codec_name[co])
        sheet.write(i, 2, width[co])
        sheet.write(i, 3, height[co])
        sheet.write(i, 4, r_frame_rate[co])
        #except IOError:
        #    print("worry happen in:" + path)
        #else:
        #    print("success")
        i = i + 1
workbook.save(f'{file_name}.xls')
'''

'''