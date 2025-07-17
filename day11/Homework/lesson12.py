#  1
for i in range(1, 50, 2):
    print("მე ვარ რიცხვი:", i)

# 2
for i in range(5):
    print("* " * 5)

# 3
i = 0
while i < 5:
    print("* " * 5)
    i += 1

# 4
for i in range(3):
    print("* " * 7)
    
for num1 in range(3):
    for num in range(2):
        print("num1 =", num1, "num =", num)

# 5
while True:
    username = input("შეიყვანე სახელი: ")
    password = input("შეიყვანე პაროლი: ")

    if username and password:
        print("რეგისტრაცია წარმატებით დასრულდა, კეთილი იყოს შენი მობრძანება,", username + "!")
    else:
        print("გთხოვ შეავსე ორივე ველი")