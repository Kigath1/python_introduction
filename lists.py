# created an empty list
my_list = []

# append the following elements 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insert the value 15 in the second position of the list 
my_list.insert(1, 15)

# extending myList with another list 
my_list.extend([50, 60, 70])

# removing the last element of the list 
my_list.pop()

# sorting the list in ascending order
my_list.sort()

# finding and printing the index of the value 30 in the list 
index_30 = my_list.index(30)
print(index_30)


print(my_list)
