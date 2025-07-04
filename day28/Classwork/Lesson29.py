
def calculate_sum(numbers):
    total_for = 0
    for num in numbers:
        total_for += num

    total_sum = sum(numbers)

    return total_for, total_sum

# magaliti
my_list = [5, 10, 15, 20]
result_for, result_sum = calculate_sum(my_list)

print("ჯამი for ციკლით:", result_for)
print("ჯამი sum() ფუნქციით:", result_sum)