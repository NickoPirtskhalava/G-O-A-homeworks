# 1)
age = int(input("რამდენი წლის ხარ? "))
for i in range(age):
    print(i)

# 2)
celsius = float(input("შეიყვანე ტემპერატურა ცელსიუსში: "))
fahrenheit = (celsius * 9 / 5) + 32
print("ტემპერატურა ფარენჰეიტში:", fahrenheit)

# 3)
print(5 > 3 and 2 < 4)
print(10 == 10 or 7 < 5)
print(not (4 <= 2))

print(8 != 8 and 1 == 1)
print(3 < 2 or 9 > 10)
print(not (6 > 2 and 1 < 5))

# 4)
for i in range(1, 6):
    print("<3 " * i)

# 5)
user_age = int(input("შეიყვანე ასაკი: "))
if user_age == 20 and True:
    print(True)
else:
    print(False)