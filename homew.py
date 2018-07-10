import random
# 1. 定义一个列表，嵌套的列表
rooms = [[], [], []]
# 2. 有一个列表，保存了 8 名老师的名字
teachers = ["A", "B", "C", "D", "E", "F", "G", "H"]
# 3. 随机把 8 名老师的名字添加到 第 1 个列表中
for name in teachers:
    # 生成一个 0 到 2 之间的随机数，用来进行随机分配办公室
    randomNum = random.randint(0,2)
    # 向 randomNum 标记的 room 中添加一个新的老师名字
    rooms[randomNum].append(name)

# 打印出当前所有办公室中的老师信息
print(rooms)
i = 1
for room in rooms:
    print("办公室%d 里面的老师姓名是:"%i)
    for name in room:
        print(name, end=" ")
    print("")
    i += 1
