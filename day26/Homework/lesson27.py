# 1)
def sum_numbers(a, b):
    print("ჯამი არის:", a + b)

sum_numbers(5, 7)

# 2)
def even_or_odd(number):
    if number % 2 == 0:
        return "ლუწია"
    else:
        return "კენტია"

print(even_or_odd(10))
print(even_or_odd(7))

# 3)
def positive_or_negative(number):
    if number > 0:
        return "დადებითია"
    elif number < 0:
        return "უარყოფითია"
    else:
        return "ნულია"

print(positive_or_negative(5))
print(positive_or_negative(-3))

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