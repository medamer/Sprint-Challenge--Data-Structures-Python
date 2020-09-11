import time
import sys

sys.path.append('./names/binary_search.py')
from binary_search import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

#binary = BSTNode(names_1)
# duplicates = binary.contains(names_2)
for i in names_1:
    binary = BSTNode(i)
    for j in names_2:
        if binary.contains(j) is True:
            duplicates.append(i)


# duplicates = [value for value in names_1 if value in names_2]
# Replace the nested for loops below with your improvements
# class Find_dup:
#     def __init__(self):
#         self.list1 = None
#         self.list2 = None
#     def find_dup(list1, list2):
#         l = []
#         for value in list1:
#             if value in list2:
#                 l.append(value)
#         return l

# duplicates = Find_dup.find_dup(names_1, names_2)

#breakpoint()
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

