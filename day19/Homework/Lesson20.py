# 1:
letters = ['ა', 'ბ', 'გ', 'დ', 'ე', 'ვ', 'ზ', 'თ', 'ი', 'კ', 'ლ', 'მ', 'ო', 'პ', 'ჟ', 'უ']
vowels = ['ა', 'ე', 'ი', 'ო', 'უ']
count = 0

for letter in letters:
    if letter in vowels:
        count += 1

print("ხმოვნების რაოდენობა:", count)
print()

# 2:
numbers = list(range(1, 51))
result = []

for num in numbers:
    if num % 5 == 0 and num % 3 == 0:
        result.append(num)

print("5-ის და 3-ის ჯერადები:", result)
print()

# 3:
mixed = ['ა', 1, 'ბ', 2, 'გ', 3]
text = ""

for item in mixed:
    text += str(item)

print("ერთ სტრინგად:", text)
print()

# 4:
print("რომბი:")
for i in range(4):
    print(" " * i + "******")
print()

# 5:
age = int(input("რამდენი წლის ხარ? "))

if age > 12:
    print("შენ არ ხარ 12 წლის")
else:
    print("შენ ხარ 12 წლის ან ნაკლები")