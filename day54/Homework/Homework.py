# 1
data = {"name": "Nicko", "age": 20, "city": "Tbilisi"}
keys = []
values = []
for k, v in data.items():
    keys.append(k)
    values.append(v)
print(keys, values)

# 2
result = [10, 43, 12, 11, 94, 10, 55, 7, 11]
unique = []
for num in result:
    if num not in unique:
        unique.append(num)
print(unique)

# 3
text = "hello world"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.replace("world", "Nicko"))
print(text.count("l"))

# 4
info = {}
key = input("Enter key: ")
value = input("Enter value: ")
info[key] = value
new_value = input("Enter new value for the key: ")
info[key] = new_value
print(info)

# 5
def remove_duplicates(lst):
    final = []
    for i in lst:
        if i not in final:
            final.append(i)
    return final

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))