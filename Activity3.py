number = int(input("Enter your number: "))

sum = 0
prod = 1

while number > 0:
    digit = number % 10
    sum += digit
    prod *= digit
    number //=10

if sum == prod:
    print("Your number is a spy number.")
else:
    print("Your number is not a spy number.")
