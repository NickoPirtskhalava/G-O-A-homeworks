# 1)
name = input("შეიყვანე შენი სახელი: ")
result = ""

for letter in name:
    result += letter + " "

print("შენი სახელი სფეისებით:", result.strip())


# 2)
start = int(input("შეიყვანე საწყისი რიცხვი: "))
end = int(input("შეიყვანე საბოლოო რიცხვი: "))

for i in range(start, end + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(i, "ეს ციფრი არის 3-ისა და 2-ის ჯერადი")
    else:
        print(i, "არაუშავს, მაინც ჩადი გამოხვალ")

# 3)
result = 0

for i in range(5):
    num = float(input(f"{i+1}) შეიყვანე რიცხვი: "))
    result += num

average = result / 5
print("საშუალო არითმეტიკული:", average)

# 4)
for i in range(-100, 101):
    if i > 0:
        print(i)

# 5)
while True:
    num = int(input("შეიყვანე დადებითი რიცხვი: "))
    if num < 0:
        print("უარყოფითი რიცხვი აღმოჩენილია. დასრულდა 💥")
        break
    else:
        print("გმადლობთ! შენ შეიყვანე:", num)
        