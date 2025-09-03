#set constructor 
# thisset = set(("Apple", "banana", "pineapple", "kiwi"))
# print(thisset)

#dublicates not allowed
# set1 = {"apple", "banana", "mango", "apple"}
# print(set1)
# print(len(set1))
# print(type(set1))

#unindexed
# print(set1[1])

#accessing set
#  for x in thisset:
#      print(x)

# print("kiwi" in thisset)
# print("orange" in thisset)

# add items
# set2 = {"apple", "banana", "mango", "orange"}
# set2.add("peach")
# print(set2)

# # #update set
# set2 = {"apple", "banana", "mango", "orange"}
# set3 = {"watermelon", "grapes"}
# # set2.update(set3)
# print(set2)

# # set2.discard("apple")
# print(set2)

# # x = set2.pop()
# print(set2)

# #clear
# # set2.clear()
# print(set2)

# # del
# # del set2
# print(set2)

# #union
# # set4 = set2.union(set3)
# # print(set4)

# set4 = set2 | set3
# print(set4)

#intersection
set_1 = {"apple", "kiwi", "oranges"}
set_2 = {"banana", "grapes", "oranges"}

# set_3 =set_1.intersection(set_2)
# print(set_3)

# #update_intersection
# set_1.intersection_update(set_2)
# print(set_1)

# set_1.difference(set_2)
# print(set_1)

set_1.symmetric_difference(set_2)
print(set_1)















