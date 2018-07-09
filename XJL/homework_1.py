import random

rooms = [[], [], []]
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

for i in teachers:
    a = random.randint(0, 2)
    rooms[a].append(i)
print(rooms)