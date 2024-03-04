my_list = [1,2,3]
my_list[2] = 200
#print(my_list)

my_list.append(50)
print(my_list)

my_list.extend([100,500])
print(my_list)

my_list.insert(0,"Santhosh")
print(my_list)

my_list.remove(100)
print(my_list)

new_list = my_list.copy()
print(new_list)

my_list.clear()
print(my_list)

new_list.sort()
print(new_list)