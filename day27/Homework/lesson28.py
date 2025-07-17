# 1)
def sum_numbers(a, b):
    print("რიცხვების ჯამი არის:", a + b)

sum_numbers(10, 15)

# 2)
def even_or_odd(number):
    if number % 2 == 0:
        return "ლუწია"
    else:
        return "კენტია"

print(even_or_odd(8))
print(even_or_odd(5))

# 3)
def check_sign(number):
    if number > 0:
        return "დადებითია"
    elif number < 0:
        return "უარყოფითია"
    else:
        return "ნულია"

print(check_sign(12))
print(check_sign(-7))
print(check_sign(0))

# 4)
def greet(name):
    print("Hello", name)

greet("Giorgi")
greet("Niko")

# 5)
def concatenate(str1, str2):
    return str1 + str2

result = concatenate("Goal ", "Oriented Academy")
print(result)