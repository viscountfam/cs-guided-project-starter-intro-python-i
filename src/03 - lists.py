"""
Lists
"""

# Lists are very similar to arrays.

# They can contain any type of variable, and they can contain as many variables as you wish.

# Lists can also be iterated over in a very simple manner.

# 1.
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])  # prints 1
print(mylist[1])  # prints 2
print(mylist[2])  # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)

# # 2. If index doesn't exist, an exception is raised
# mylist = [1,2,3]
# print(mylist[10])


"""
YOU DO
2 minute timer
"""
# create a `numbers` list
# use `append` to add three numbers to the list
# create a `strings` list
# use `append` to add three strings to the list
# create a `names` list that contains three different first names as strings
# Print out the first number, second string, and third name with one print statement
