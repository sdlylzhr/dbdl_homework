#把teacher数组中的老师随机分配到rooms中
#rooms = [[],[],[]]
#teachers = ["A","B","C","D","E","F","G","H","I","J","K"]

#导入包,并产生随机数
import random

rooms = []
teachers = ["A","B","C","D","E","F","G","H","I","J","K"]
copyTeachers = teachers
tlen = len(teachers)
num1 = random.randint(0,tlen)
room1 = []
i=0
numlen = num1
while i < num1:
    randnum = random.randint(0,numlen)
    room1.append(copyTeachers[randnum])
    copyTeachers.remove(copyTeachers[randnum])
    numlen-=1
    i+=1
ctlen = len(copyTeachers)
num2 = random.randint(0,ctlen)
room2 = []
j=0
numlen = num2
if ctlen != 0:
    while j < num2:
        randnum = random.randint(0, numlen)
        room2.append(copyTeachers[randnum])
        copyTeachers.remove(copyTeachers[randnum])
        numlen -= 1
        j += 1
room3 = []
room3.extend(copyTeachers)
rooms.append(room1)
rooms.append(room2)
rooms.append(room3)
print("end = ",end="")
print(rooms)
