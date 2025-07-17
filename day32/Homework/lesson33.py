# 1)
indexebi = [1,2,3,4,5]
indexebi.pop(2)

print(indexebi)

indexebi2 = [1,2,3,4,5]
indexebi2.insert(0,0)

print(indexebi2)

# 2)
def numbers(num1, num2):
    return num1 ** num2

print(numbers(10, 2))

# 3)
def variable(var):
    if len(var) %2 == 0:
        return "List length is even"
    else:
        return "List length is odd"
    
print(variable([1,2,3,4,5,6]))