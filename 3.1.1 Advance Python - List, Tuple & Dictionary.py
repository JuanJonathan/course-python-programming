# List
list1 = ["apple", "banana", "watermelon"]
list2 = [2, 1, 2, 7, 4, 10]
list3 = [True, False, True]
list4 = ["abc", 10, True, 40, "male"]

list5 = [list1 + list2]
print(list5)

print(list2 + list2)

list2.sort()

print(list2)

list1.sort()
print(list1)

list2.reverse()
print(list2)

list6 = list2.copy()
print(list6)

print(list2.count(7))


fruit_list = ["apple", "banana", "watermelon", "orange", "mango", "cerry", "pineapple"]
print(fruit_list[1:4])
print(fruit_list[-3:])

fruit_list[2] = "avocado"
print(fruit_list)

# Membership test
print('watermelon' in fruit_list)
print('watermelon' not in fruit_list)



# Append
fruit_list = ["apple", "banana", "watermelon"]
fruit_list.append("orange")

print(fruit_list)

# Insert
fruit_list.insert(1, "mango")
print(fruit_list)

# Extend
fruit_list1 = ["apple", "banana"]
fruit_list2 = ["watermelon", "orange"]
fruit_list1.extend(fruit_list2)
print(fruit_list1)

# Remove
fruit_list = ["apple", "banana", "watermelon", "orange", "mango", "cerry", "pineapple"]
fruit_list.remove("orange")
print(fruit_list)

# Pop
fruit_list = ["apple", "banana", "watermelon", "orange", "mango", "cerry", "pineapple"]
fruit_list.pop(2)
print(fruit_list)

# Del
fruit_list = ["apple", "banana", "watermelon", "orange", "mango", "cerry", "pineapple"]
del fruit_list[3]
print(fruit_list)

# Clear
fruit_list = ["apple", "banana", "watermelon", "orange", "mango", "cerry", "pineapple"]
fruit_list.clear()
print(fruit_list)