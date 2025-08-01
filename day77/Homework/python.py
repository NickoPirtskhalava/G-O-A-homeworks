# 1)
number = int(input("შეიყვანეთ რიცხვი: "))
if number % 2 == 0:
    print("ლუწია")
else:
    print("კენტია")


# 2)
age = int(input("შეიყვანეთ თქვენი ასაკი: "))
if age < 18:
    print("თქვენ მიიღეთ 50%-იანი ფასდაკლება")
else:
    print("თქვენ არ მიიღეთ ფასდაკლება")


# 3)
age = int(input("შეიყვანეთ თქვენი ასაკი: "))
if age < 18:
    print("თქვენ მიიღეთ 50%-იანი ფასდაკლება")
elif age == 18:
    print("თქვენ მიიღეთ 25%-იანი ფასდაკლება")
else:
    print("თქვენ არ მიიღეთ ფასდაკლება")


# 4)
# ცვლადს აქვს True მნიშვნელობა როცა მასში არის ნებისმიერი მნიშვნელობა გარდა:
# - ცარიელი სტრინგი ""
# - 0
# - None
# - False
# - ცარიელი სია [], ცარიელი ლექსიკონი {}, ცარიელი tuple ()
# მაგალითად:
x = ""
print(bool(x))  # False

x = "Nicko"
print(bool(x))  # True


# 5)
name = input("შეიყვანეთ თქვენი სახელი: ")
if len(name) > 6:
    print(f"hello my friend {name}!")
else:
    print(f"hello {name}!")