# 1)
age = int(input("შეიყვანეთ თქვენი ასაკი: "))
if age <= 14:
    print("you are kid")
elif age <= 18:
    print("you are not adult yet")
else:
    print("you are adult")

# 2)
name = ""
if name:
    print(f"Hello {name}!")
else:
    name = "guest"
    print(f"Hello {name}!")

# 3)
name = input("შეიყვანეთ თქვენი სახელი: ")
age = int(input("შეიყვანეთ თქვენი ასაკი: "))
if age <= 18:
    print(f"you are not adult yet {name}!")
else:
    print(f"Hello {name}!")