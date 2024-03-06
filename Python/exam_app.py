def exam_calculator(satir):
    satir = satir[:-1]
    liste = satir.split(':')
    studentName = liste[0]
    exams = liste[1].split(',')
    
    exam1= int(exams[0])
    exam2= int(exams[1])
    exam3= int(exams[2])

    average = (exam1 + exam2 + exam3)/3
    
    if average>=90 and average<=100:
        harf = "AA"
    elif average>=85 and average<=89:
        harf = "BA"
    elif average>=80 and average<=84:
        harf = "BB"
    elif average>=75 and average<=79:
        harf = "CB"
    elif average>=70 and average<=74:
        harf = "CC"
    elif average>=65 and average<=69:
        harf = "CD"
    elif average>=60 and average<=64:
        harf = "DD"
    elif average>=55 and average<=59:
        harf = "DF"        
    else:
        harf = "FF"
    return studentName + ": " + harf + "\n"
        
def average_read():
    with open('exams.txt',"r",encoding="utf-8") as file:
        for satir in file:
            print(exam_calculator(satir))

def exam_input():
    name = input('Student name: ')
    surname = input('Student surname: ')
    exam1 = input('exam 1: ')
    exam2 = input('exam 2: ')
    exam3 = input('exam 3: ')
    
    with open("exams.txt","a",encoding="utf-8") as file:
        file.write(name+' '+surname+':'+exam1+','+exam2+','+exam3+'\n')

def exam_record():
    with open('exams.txt',"r",encoding="utf-8") as file:
        liste = []
        
        for i in file:
            list.append(exam_calculator(i))
        with open("result.txt","w",encoding="utf-8") as file2:
            for i in list:
                file2.write(i)

while True:
    process = input("1- Exams read\n2- Exam input\n3- Exam record\n4-Exit\n")
    
    if process == '1':
        average_read()
    elif process == '2':
        exam_input()
    elif process == '3':
        exam_record()
    else:
        break
    