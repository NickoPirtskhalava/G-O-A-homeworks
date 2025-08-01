# 1
car = {
    "brand": "BMW",
    "model": "M3",
    "year": 2022
}
print(car.items())
print(car.keys())
print(car.values())

# 2
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))
print(a.difference(b))
print(a.intersection(b))

# 3
info = {"name": "Nicko", "age": 20, "country": "Georgia"}
for value in info.values():
    print(value)

# 4
# Dictionary ინახავს Key/Value წყვილებს.
# Set ინახავს მხოლოდ უნიკალურ ელემენტებს.

# 5
person = {"name": "Nicko", "age": 20, "city": "Tbilisi"}
output = []
for k, v in person.items():
    output.append(k)
    output.append(v)
print(output)

# 6
data = {"name": "Nicko", "age": 20, "city": "Tbilisi"}
key = input("Enter key: ")
value = input("Enter value: ")
if key not in data:
    data[key] = value
else:
    print("Key already exists!")
print(data)