"""
All methods for list
"""
list_example = [3, 2, 1, 5, 4]

print(f"First element: {list_example[0]}")

# list methods
print(f"Sorted funtion on list is not in-place {sorted(list_example)}")
print(f"{list_example}")
print(f"{list_example.sort()} sort in place returns None {list_example}")
list_example.append(6)
print(f"append: {list_example}")

list_example.extend([4,2])
print(f"append: {list_example}")

#insert list_example.insert(i, x)
list_example.insert(2,2)
print(f"append: {list_example}")