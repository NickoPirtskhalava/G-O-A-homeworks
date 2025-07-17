# 1)
even_numbers = []
for i in range(0, 201):
    if i % 2 == 0:
        even_numbers.append(i)
print("ლუწი რიცხვები:", even_numbers)

# 2)
favorite_names = []
for i in range(5):
    name = input("შეიყვანე შენი საყვარელი სახელი: ")
    favorite_names.append(name)
print("შენი საყვარელი სახელები:", favorite_names)

# 3)
my_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
odd_index_elements = []
for i in range(len(my_list)):
    if i % 2 != 0:
        odd_index_elements.append(my_list[i])
print("კენტ ინდექსზე მდგომი ელემენტები:", odd_index_elements)

# 4)
text = "Goal Oriented Academy"
length = len(text)
print("სტრინგის სიმბოლოების რაოდენობა:", length)

# 5)
numbers = [10, 20, 30, 40, 50]
index = int(input("შეიყვანე ინდექსი (0-დან 4-მდე): "))
if 0 <= index < len(numbers):
    numbers.pop(index)
    print("განახლებული სია:", numbers)
else:
    print("არასწორი ინდექსი")

# 6)
some_list = [1, 2, 3, 4, 5, 6]
print("სიის სიგრძე:", len(some_list))