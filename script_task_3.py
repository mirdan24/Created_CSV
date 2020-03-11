import csv
from time import sleep
exampleFile = open('test.csv')
exampleReader = csv.reader(exampleFile, delimiter = ';')
editFile = open('test_utilization.csv','w',newline='',encoding='utf-8')
edifFileWriter = csv.writer(editFile,delimiter=';', lineterminator = '\n')
exampleFileClass = open('class.csv',encoding='utf-8')
exampleReaderClass = csv.reader(exampleFileClass,delimiter = ';')

class_numbs = []
edifFileWriter.writerow(['class_id','class_name','teaching_hours','test_created_at','test_authorized_at','test_id','test_level','class_test_number'])
for class_num in exampleReader:
    if(class_num[2]=='class_id'): continue
    elif(int(class_num[2]) not in class_numbs):
        class_numbs.append(int(class_num[2]))
    else: continue
class_numbs.sort()

list_of_names = []
list_of_hours = []
for name in exampleReaderClass:
    if(name[0]=='id'): continue
    elif (int(name[0]) in class_numbs):
        list_of_names.append(name[3])
        list_of_hours.append(name[6])

i = 0
num_id = 1
class_test_number = 0
# print(int(class_numbs[(len(class_numbs))-1]))
print("making frequency teach database...")
datetimeFormat = '%d.%m.%Y %H:%M'
while i<=(len(class_numbs)-1):
    exampleFile = open('edit_test.csv')
    exampleReader = csv.reader(exampleFile, delimiter = ';')
    for row in exampleReader:
        if (row[2]=='class_id'): continue
        elif ((class_numbs[i] == int(row[2]))and(row[9]!='')):
            class_test_number += 1           
            edifFileWriter.writerow([row[2],list_of_names[i],list_of_hours[i].replace('-','--'),str(num_id),str(row[3].replace(" ","-")),str(row[9].replace(" ","-")),row[15],str(class_test_number)])
            num_id +=1
    class_test_number = 0
    i+=1
print('Done')

editFile.close()