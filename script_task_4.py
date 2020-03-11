import csv
exampleFile = open('test.csv')
exampleReader = csv.reader(exampleFile, delimiter = ';')
editFile = open('test_average_scores.csv','w',newline='',encoding='utf-8')
edifFileWriter = csv.writer(editFile,delimiter=';', lineterminator = '\n')
exampleFileClass = open('class.csv',encoding='utf-8')
exampleReaderClass = csv.reader(exampleFileClass,delimiter = ';')


edifFileWriter.writerow(['class_id','class_name','teaching_hours','test_created_at','test_authorized_at','avg_class_test_overall_score'])
class_numbs = []
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


import datetime
datetimeFormat = '%d.%m.%Y %H:%M'
i = 0
count_students = 0
score_decimal = 0
score_unity = 0
sum_of_score = 0
created = ''
authorized = ''
print("start of counting the average grade for the class...")
while i<=(len(class_numbs)-1):
    exampleFile = open('edit_test.csv')
    exampleReader = csv.reader(exampleFile, delimiter = ';')
    score = 0
    sum_of_score = 0
    count_students = 0
    for row in exampleReader:
        if (row[2]=='class_id'): continue
        elif ((row[7] == 'SCORING_SCORED')and(row[9]!='')and((class_numbs[i] == int(row[2])))):
            if row[6] == '':
                sum_of_score += 0
            else:
                sum_of_score += float(row[6])
            created = str(row[3].replace(" ","-"))
            authorized = str(row[9].replace(" ","-"))
            count_students +=1
    hours_teaching_max = 0
    hours_teaching_min = 0 
    if count_students == 0:
        if (list_of_hours[i]=='1-3'):
            hours_teaching_min = str(count_students*int(list_of_hours[i][0]))+'--'
            hours_teaching_max = str(count_students*int(list_of_hours[i][2]))
        elif (list_of_hours[i]=='3-5'):
            hours_teaching_min = str(count_students*int(list_of_hours[i][0]))+'--'
            hours_teaching_max = str(count_students*int(list_of_hours[i][2]))
        elif (list_of_hours[i]=='6-10'):
            hours_teaching_min = str(count_students*int(list_of_hours[i][0]))+'--'
            hours_teaching_max = str(count_students*int(list_of_hours[i][2:4]))
        elif (list_of_hours[i]=='11-15'):
            hours_teaching_min = str(count_students*int(list_of_hours[i][0:2]))+'--'
            hours_teaching_max = str(count_students*int(list_of_hours[i][3:5]))
        elif (list_of_hours[i]=='15+'):
            hours_teaching_min = str(count_students*int(list_of_hours[i][0:2]))+'+'
            hours_teaching_max = ''
        else:
            hours_teaching_min = '0'
            hours_teaching_max = ''
        edifFileWriter.writerow([class_numbs[i],list_of_names[i],hours_teaching_min+hours_teaching_max,created,authorized,'No results'])
    else:
        if (list_of_hours[i]=='1-3'):
            hours_teaching_min = str(count_students*int(list_of_hours[i][0]))+'--'
            hours_teaching_max = str(count_students*int(list_of_hours[i][2]))
        elif (list_of_hours[i]=='3-5'):
            hours_teaching_min = str(count_students*int(list_of_hours[i][0]))+'--'
            hours_teaching_max = str(count_students*int(list_of_hours[i][2]))
        elif (list_of_hours[i]=='6-10'):
            hours_teaching_min = str(count_students*int(list_of_hours[i][0]))+'--'
            hours_teaching_max = str(count_students*int(list_of_hours[i][2:4]))
        elif (list_of_hours[i]=='11-15'):
            hours_teaching_min = str(count_students*int(list_of_hours[i][0:2]))+'--'
            hours_teaching_max = str(count_students*int(list_of_hours[i][3:5]))
        elif (list_of_hours[i]=='15+'):
            hours_teaching_min = str(count_students*int(list_of_hours[i][0:2]))+'+'
            hours_teaching_max = ''
        else:
            hours_teaching_min = '0'
            hours_teaching_max = ''
        score_unity = (sum_of_score/count_students)
        score_decimal = (score_unity%1)
        # print(type(score))
        edifFileWriter.writerow([class_numbs[i],list_of_names[i],hours_teaching_min+hours_teaching_max,created,authorized,(str(score_unity)[:3].replace(".",",")+str(round(score_decimal,1))[2:].replace(".",","))])
        print(score_unity,score_decimal)
    i += 1
print("Done")


editFile.close()