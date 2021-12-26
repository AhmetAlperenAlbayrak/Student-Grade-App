
def grade_comp(line):
    line = line[:-1]
    list = line.split(':')
    
    studentName = list[0]
    grades = list[1].split(',')
    
    grade1 = int(grades[0])
    grade2 = int(grades[1])
    grade3 = int(grades[2])

    gpa = (grade1+grade2+grade3) / 3

    if gpa >= 90 and gpa <= 100:
        letter = 'AA'
    elif gpa >= 85 and gpa <=89:
        letter = 'BA'
    elif gpa >= 75 and gpa <=84:
        letter = 'BB'
    elif gpa >= 65 and gpa <=74:
        letter = 'CC'
    elif gpa >= 45 and gpa <=64:
        letter = 'DD'
    else:
        letter= 'FF'
    return studentName + ':' + letter + '\n'

def read_gpa():
    with open('Student Notes.txt', 'r', encoding= 'utf-8' ) as file:
        for line in file:
            print(grade_comp(line))
def input_gpa():
    name = input('Student Name: ')
    surname = input('Student Surname: ')
    grade1 = input('1st Grade: ')
    grade2 = input('2nd Grade: ')
    grade3 = input('3rd Grade: ')

    with open('Student Notes.txt', 'a', encoding= 'utf-8' ) as file:
        file.write(name + ' ' + surname + ':' + grade1 + ',' + grade2 + ',' + grade3+ '\n')
def save_gpa():
    with open('Student Notes.txt', 'a', encoding= 'utf-8' ) as file:
        list = []

        for i in file:
            list.append(grade_comp[i])
        
        with open('results.txt', 'w',encoding= 'utf-8' ) as file2:
            for i in list:
                file2.write(i)  
while True:
    sum = input('1- Read the Scores\n2-Input the Scores\n3-Save the Scores\n4- Exit\n')

    if sum == '1':
        read_gpa()
    elif sum == '2':
        input_gpa()
    elif sum == '3':
        save_gpa()
    else:
        break