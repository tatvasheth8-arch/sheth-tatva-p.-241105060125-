print("Number Rotation Checker")

num = int(input("Enter number: "))

digits = 0
temp = num

while temp > 0:
    digits = digits + 1
    temp = temp // 10

power = 10 ** (digits - 1)

last = num % 10
rotated = (last * power) + (num // 10)

print("Rotated Number:", rotated)

if rotated == num:
    print("Same number")
else:
    print("Different number")

if digits < 2:
    print("Single digit")
else:
    print("Multiple digits")
