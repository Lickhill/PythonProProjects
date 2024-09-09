my_list = [5, 2, 8, 1, 9]
print("Original List:", my_list)

my_list.append(10)
print("After append(10):", my_list)

my_list.extend([11, 12])
print("After extend([11, 12]):", my_list)

my_list.insert(2, 7)
print("After insert(2, 7):", my_list)

my_list.remove(2)
print("After remove(2):", my_list)

popped_item = my_list.pop(3)
print("Popped item:", popped_item)
print("List after pop(3):", my_list)

index_of_8 = my_list.index(8)
print("Index of 8:", index_of_8)

count_of_1 = my_list.count(1)
print("Count of 1:", count_of_1)

my_list.sort()
print("Sorted list:", my_list)

my_list.reverse()
print("Reversed list:", my_list)

my_list.clear()
print("List after clear():", my_list)

my_list = [5, 2, 8, 1, 9]

max_value = max(my_list)
print("Max value:", max_value)

min_value = min(my_list)
print("Min value:", min_value)

total_sum = sum(my_list)
print("Sum of list:", total_sum)

sliced_list = my_list[1:4]
print("Sliced list (from index 1 to 3):", sliced_list)

count_of_5 = my_list.count(5)
print("Count of 5:", count_of_5)

index_of_8 = my_list.index(8)
print("Index of 8:", index_of_8)
