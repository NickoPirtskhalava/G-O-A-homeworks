# 1.
age = int(input("შეიყვანეთ თქვენი წლოვანება: "))
is_teenager = age > 13 and age < 19
print("თინეიჯერია:", is_teenager)

# 2.
grade = int(input("ნუგზარ, შეიყვანე საკონტროლოზე მიღებული ნიშანი (1-10): "))
is_A = grade >= 9
is_B = grade >= 8 and grade < 9
is_C = grade >= 7 and grade < 8
is_D = grade >= 6 and grade < 7
is_F = grade < 6
print("A:", is_A)
print("B:", is_B)
print("C:", is_C)
print("D:", is_D)
print("F:", is_F)

# 3.
x = True
y = False
print("x AND y:", x and y)
print("x OR y:", x or y)
print("NOT x:", not x)
print("NOT y:", not y)
print("XOR (ერთ-ერთი True):", (x and not y) or (not x and y))

# 4.
num1 = int(input("შეიყვანე პირველი რიცხვი: "))
num2 = int(input("შეიყვანე მეორე რიცხვი: "))
print("== :", num1 == num2)
print("<  :", num1 < num2)
print(">  :", num1 > num2)
print("<= :", num1 <= num2)
print(">= :", num1 >= num2)
print("!= :", num1 != num2)

# 5.
a = 12
b = 7
c = 3
is_a_greatest = a > b and a > c
is_b_middle = (b > a and b < c) or (b < a and b > c)
is_c_least = c < a and c < b
print("a უდიდესია:", is_a_greatest)
print("b საშუალოა:", is_b_middle)
print("c უმცირესია:", is_c_least)

# 6.
score = int(input("შეიყვანე ქულა (0-100): "))
is_pass = score >= 50
is_high_pass = score > 75 and score < 90
is_perfect = score == 100
is_failing = score < 50
print("გავიდა:", is_pass)
print("მაღალი შეფასება:", is_high_pass)
print("იდეალურია:", is_perfect)
print("ჩაჭრა:", is_failing)

# 7.
P = True
Q = False
P_and_not_Q = P and not Q
not_P_and_Q = not P and Q
P_xor_Q = (P and not Q) or (not P and Q)
print("P და არა Q:", P_and_not_Q)
print("არა P და Q:", not_P_and_Q)
print("XOR:", P_xor_Q)