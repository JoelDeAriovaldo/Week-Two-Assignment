# Creating an empty list
my_list = []

# Adding elements to a list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

# Inserting the value 15 in the second position of the list
my_list.insert(1, 15)

print(my_list)

# Adding another list to the original list
my_list.extend([50, 60, 70])

print(my_list)

# Removing the last element from the list
my_list.pop()
print(my_list)

# Sorting the list in ascending order
my_list.sort()
print(my_list)

# Finding and printing the index of the value 30 in the list
print(my_list.index(30))