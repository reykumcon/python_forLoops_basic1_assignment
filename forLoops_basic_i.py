#1 Basic

for i in range(150):
    print(i)

#2 Multiples of Five

for j in range(5, 1000):
    if j % 5 == 0:
        print(j)

#3 Counting, the Dojo Way

for k in range(1, 100):
    if k % 10 == 0:
        print("Coding Dojo")
    elif k % 5 == 0:
        print("Coding")

#4 Whoa. That Sucker's Huge

sum = 0

for x in range(1, 500000):
    if x % 2 == 1:
        sum += x

print(sum)

#5 Countdown by Fours
for y in range(2018, 0, -4):
    print(y)

#6 Flexible Counter
lowNum = int(input("Enter a low number: "))
highNum = int(input("Enter a high number: "))
mult = int(input("Enter a multiplier: "))

for z in range(lowNum, highNum + 1):
    if z % mult == 0:
        print(z)