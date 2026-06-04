num1 = int(input("Enter Largest number : "))
num2 = int(input("Enter Smallest number : "))

largest = max(num1, num2)

while True:

    if largest % num1 == 0 and largest % num2 == 0:
        lcm = largest
        break

    largest = largest + 1

print("LCM is :", lcm)