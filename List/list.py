#List
# A list in Python is an ordered, mutable collection
# that allows storing multiple data items (of any type) in a single variable.
# It supports indexing, slicing, and dynamic resizing,
# making it ideal for tasks like iteration, modification,
# and organization of data in a flexible and efficient way.
# Lists are one of the most versatile data structures in Python!


# Syntax: list_name = [element1, element2, element3]

# pets = []

fruits = ['apple', 'banana', 'cherry']

#print(fruits[6])

# Slicing
fruits = ['apple', 'banana', 'cherry', 'mango', 'grape']
# print(len(fruits))
# print(fruits[2:9])


# Adding
fruits = ['apple', 'banana', 'cherry']

# fruits.append('kumquat')
# fruits.insert(13, 'kumquat')
# print(fruits)


# Removing
fruits = ['apple', 'banana', 'cherry']

# del fruits[1:3]
# print(fruits)
# #fruits.remove('banana')
# print(fruits)



# Update
fruits = ['apple', 'banana', 'cherry']
fruits[0] = 'kiwi'  # Update the first element


# Nested List
fruits = [['apple', 'banana'], ['cherry', 'mango'], 'grape']
# print(fruits[0])
# print(fruits[0][1])
# print(fruits[-1])


# Sorting: Arranges the elements of a list in a specific order (either ascending or descending)
fruits = ['apple', 'banana', 'cherry', 'mango', 'grape']
fruits.sort()
print('sorted', fruits)
fruits.sort(reverse=True)
print('sorted reversed', fruits)

#Reverse: Reverses the order of elements in the list, without arranging them in any specific order
fruits.reverse()
print('reverse', fruits)

# Extending a List
fruits = ['apple', 'banana']
fruits2 = ['orange']
fruits.extend(fruits2)
print(fruits)

# Max, Min, and Sum
list_example = [1, 5, 6, 34]

# print(max(list_example))
# print(min(list_example))
# print(sum(list_example))
#
#
# nums = ["1", "53", "21"]
# nums.sort()
# print(nums)