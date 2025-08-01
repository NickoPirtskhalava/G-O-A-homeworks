# 1)
def print_numbers(number):
    for i in range(number + 1):
        print(i)

# 2)
def greet(name, age):
    if age < 18:
        return "your not adult yet"
    else:
        return f"Hello {name}!"

# 3)
def show_letters(name):
    for letter in name:
        print(letter)