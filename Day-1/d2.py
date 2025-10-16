# 1. Print numbers 1 to 10 using for loop
print("1. Numbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print("\n" + "-" * 40)

# 2. Print even numbers 2 to 20 using while loop
print("2. Even numbers from 2 to 20:")
num = 2
while num <= 20:
    print(num, end=" ")
    num += 2
print("\n" + "-" * 40)

# 3. Print multiplication table of 5
print("3. Multiplication Table of 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
print("-" * 40)

# 4. Print each character of your name
print("4. Each character of your name:")
name = "Sam"   # ← Replace with your own name if you like
for ch in name:
    print(ch)
print("-" * 40)

# 5. Print all numbers divisible by 3 and 5 between 1–100
print("5. Numbers divisible by both 3 and 5 (1–100):")
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
print("\n" + "-" * 40)
