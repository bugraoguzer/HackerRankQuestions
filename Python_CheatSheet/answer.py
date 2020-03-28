if __name__ == '__main__':
    students = {}
    min = 100
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students[name]=score
      
def minimumfounder(students,number):
    global min2
    global lowest2
    min2 = 100
    for key,value in students.items():
            if(value <= min2):
                min2 = value
                lowest2 = key
    if(number==1):
        return lowest2
    else:
        return min2

def organizer(students):
    list21=[]
    minimum = minimumfounder(students,2)
    for key,value in students.items():
        if(value==minimum):
            list21.append(key)
    for i in sorted(list21):
        print(i)

       
minimum23 = minimumfounder(students,2)
while (minimum23 == minimumfounder(students,2)):
    students.pop(minimumfounder(students,1))

organizer(students)
