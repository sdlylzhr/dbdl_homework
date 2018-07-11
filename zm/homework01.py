import random

rooms = [[],[],[]]
teachers = ["A","B","C","D","E","F","G","H","I","J","K"]
for i in range(0,11):
    a = random.randint(0,2)
    rooms[a].append(teachers[i])
print(rooms)