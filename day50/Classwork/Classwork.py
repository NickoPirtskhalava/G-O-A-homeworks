# 1)
# tuple უცვლელია — ვერ შეცვლი ელემენტებს.
# list კი შეცვლადია.
# tuple იყენებს (), ხოლო list — []

# 2)
movies = ("Inception", "Interstellar", "The Matrix", "Parasite", "Spirited Away")
print(movies[0])
print(movies[-1])

# 3)
weekdays = ("ორშაბათი", "სამშაბათი", "ოთხშაბათი", "ხუთშაბათი", "პარასკევი", "შაბათი", "კვირა")
(mon, tue, wed, thu, fri, sat, sun) = weekdays

print(mon)
print(tue)
print(wed)
print(thu)
print(fri)
print(sat)
print(sun)

# 4)
colors = ("წითელი", "ლურჯი", "მწვანე", "ყვითელი")
print("მწვანე" in colors)
print("იისფერი" in colors)

# 5)
fruits = ("banana", "cherry", "strawberry", "raspberry")
(first, *second, third) = fruits

print(first)
print(second)
print(third)