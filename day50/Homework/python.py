# 1)
items = ("milk", "bread", "eggs", "apples")
item1, item2, item3, item4 = items
print(item1)
print(item2)
print(item3)
print(item4)

# 2)
food = ("burger", "fries", "soda")
food_list = list(food)
food_list.extend(["salad", "fruit", "water"])
updated_food = tuple(food_list)
print(updated_food)

# 3)
# ასტრიქსი (*) დაშლისას გამოიყენება, რომ ბევრ ელემენტს ერთ სიაში შეინახოს.
# მაგ: (first, *middle, last) — middle იქნება სია, სადაც შუა ელემენტები წავლენ.

# 4)
months = ("January", "February", "March", "April", "May")
(first, second, third, *fourth) = months

print(first)
print(second)
print(third)
print(fourth)