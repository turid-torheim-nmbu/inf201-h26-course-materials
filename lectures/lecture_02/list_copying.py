# A small script about copying lists
# Turid  Torheim, NMBU

from copy import deepcopy

list1 = [1, 2, 3, 4, 5]
list2 = list1

print(f"list1 is at {id(list1)}")
print(f"list2 is at {id(list2)}")

list3 = list1.copy()
print(f"list3 is at {id(list3)}")

list4 = list1[:]
print(f"list4 is at {id(list4)}")

nested_list1 = [1, 2, [3, 4], 5]
print(f"nested_list1 is at {id(nested_list1)}")

nested_list2 = nested_list1.copy()
print(f"nested_list2 is at {id(nested_list2)}")

nested_list2[2][0] = 0
print(nested_list2)
print(nested_list1)

print(f"nested_list1 element 2 is at {id(nested_list1[2])}")
print(f"nested_list2 element 2 is at {id(nested_list2[2])}")

nested_list2[2][0] = 3
print(nested_list1)
print(nested_list2)

nested_list3 = deepcopy(nested_list1)
print(nested_list3)
print(f"nested_list3 is at {id(nested_list3)}")

nested_list3[2][0] = 0
print(nested_list3)
print(nested_list1)
print(nested_list2)
