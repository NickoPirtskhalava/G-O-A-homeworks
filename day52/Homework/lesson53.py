# 2
# List ინახავს დუპლიკატებს და ინდექსირებადია; Set ინახავს მხოლოდ უნიკალურ ელემენტებს და ინდექსირება არ შეუძლია.
# List არის დალაგებული, ხოლო Set — არ არის.

# 3
numbers = {1, 2, 3, 4}
# print(numbers[0]) 
numbers.remove(2)
numbers.add(22)
print(numbers)

# 4
foods = {"burger", "fries", "soda"}
foods.clear()
foods.update({"salad", "nuts", "quinoa"})
print(foods)

# 5
def remove_duplicates(input_list):
    return list(set(input_list))

list1 = [7, 5, 44, 14, 5, 5, 44]
list2 = [89, 90, 56, 45, 90, 78, 90]

print(remove_duplicates(list1))
print(remove_duplicates(list2))