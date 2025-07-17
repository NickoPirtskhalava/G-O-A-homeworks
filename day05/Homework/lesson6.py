# 1)
birth_year = int(input("შეიყვანეთ თქვენი დაბადების წელი: "))
current_year = 2025
age = current_year - birth_year
print("თქვენი წლოვანებაა:", age, "წელი.")

# 2)
length = float(input("შეიყვანეთ ოთხკუთხედის სიგრძე: "))
width = float(input("შეიყვანეთ ოთხკუთხედის სიგანე: "))

area = length * width
perimeter = 2 * (length + width)

print("ოთხკუთხედის ფართობია:", area)
print("ოთხკუთხედის პერიმეტრია:", perimeter)

# 3)
distance_km = float(input("შეიყვანეთ მანძილი სახლიდან სკოლამდე კილომეტრებში: "))

distance_m = distance_km * 1000
distance_cm = distance_m * 100
distance_mm = distance_cm * 10

print("მანძილი მეტრებში:", distance_m, "მეტრი")
print("მანძილი სანტიმეტრებში:", distance_cm, "სანტიმეტრი")
print("მანძილი მილიმეტრებში:", distance_mm, "მილიმეტრი")

# 4)
name = input("შეიყვანეთ თქვენი სახელი: ")
surname = input("შეიყვანეთ თქვენი გვარი: ")
parent_name = input("შეიყვანეთ თქვენი მშობლის სახელი: ")
parent_surname = input("შეიყვანეთ თქვენი მშობლის გვარი: ")
fav_color = input("შეიყვანეთ თქვენი საყვარელი ფერი: ")
fav_car = input("შეიყვანეთ თქვენი საყვარელი მანქანა: ")
hobby1 = input("შეიყვანეთ თქვენი 1-ლი საყვარელი ჰობი: ")
hobby2 = input("შეიყვანეთ თქვენი მე-2 საყვარელი ჰობი: ")
hobby3 = input("შეიყვანეთ თქვენი მე-3 საყვარელი ჰობი: ")
print("მე ვარ " + name + " " + surname + ", ჩემი მშობლები არიან " + parent_name + " " + parent_surname + ". ჩემი საყვარელი ფერია " + fav_color + ", საყვარელი მანქანაა " + fav_car + ", და ჩემი ჰობია " + hobby1 + ", " + hobby2 + " და " + hobby3 + ".")



# 5)
two_digit_number_str = input("შეიყვანეთ ორნიშნა რიცხვი (მაგ. 23): ")
two_digit_number = int(two_digit_number_str)

digit1 = two_digit_number // 10
digit2 = two_digit_number % 10

sum_of_digits = digit1 + digit2
print("ციფრების ჯამია:", sum_of_digits)