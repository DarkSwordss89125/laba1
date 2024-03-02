zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
zoo.insert(1,'bear')
print(zoo)
birds = ['rooster', 'ostrich', 'lark', ]
zoo.extend(birds)
print(zoo)
zoo.remove("elephant")
print(zoo)
index1=zoo.index("lion")+1
index2=zoo.index("lark")+1
print(index1)
print(index2)