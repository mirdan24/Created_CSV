import csv

exampleFile = open('test.csv')
exampleReader = csv.reader(exampleFile, delimiter = ';')
editFile = open('edit_test.csv','w',newline='')
edifFileWriter = csv.writer(editFile,delimiter=';', lineterminator = '\n')

id_test = []
student_id = []
class_id = []
created_at = []
update_at = []
last_event = []
overall_score = []
test_status = []
institution_id = []
authorized_at = []
confidence_level = []
speaking_score = []
writing_score = []
reading_score = []
listening_score = []
test_level = []
license_id = []

for row in exampleReader:
    variable_id_test = row[0]
    variable_student_id = row[1]
    variable_class_id = row[2]
    variable_created_at = row[3]
    variable_update_at = row[4]
    variable_last_event = row[5]
    variable_overall_score = row[6]
    variable_test_status = row[7]
    variable_institution_id = row[8]
    variable_authorized_at = row[9]
    variable_confidence_level = row[10]
    variable_speaking_score = row[11]
    variable_writing_score = row[12]
    variable_reading_score = row[13]
    variable_listening_score = row[14]
    variable_test_level = row[15]
    variable_license_id = row[16]

    id_test.append(variable_id_test)
    student_id.append(variable_student_id)
    class_id.append(variable_class_id) 
    created_at.append(variable_created_at)
    update_at.append(variable_update_at)
    last_event.append(variable_last_event)
    overall_score.append(variable_overall_score)
    test_status.append(variable_test_status)
    institution_id.append(variable_institution_id)
    authorized_at.append(variable_authorized_at)
    confidence_level.append(variable_confidence_level)
    speaking_score.append(variable_speaking_score)
    writing_score.append(variable_writing_score)
    reading_score.append(variable_reading_score)
    listening_score.append(variable_listening_score)
    test_level.append(variable_test_level)
    license_id.append(variable_license_id)

error_student = []
error_class = []
errorIndex = []
i = 0
for check in range(len(id_test)):
    if ((student_id[check] in error_student) and (class_id[check] in error_class)):
        errorIndex.append(i)
    else: 
        error_class.append(class_id[check])
        error_student.append(student_id[check])
    i+=1



print("in processing...")
for row in range(i):
    if (row in errorIndex):
        continue
    else:
        edifFileWriter.writerow([id_test[row],student_id[row],class_id[row],created_at[row],update_at[row],last_event[row],overall_score[row],test_status[row],institution_id[row],authorized_at[row],confidence_level[row],speaking_score[row],writing_score[row],reading_score[row],listening_score[row],test_level[row],license_id[row]])


editFile.close()
print("Done")