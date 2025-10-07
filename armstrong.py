num = int(input("Enter a number: "))
original_num = num
sum_of_powers = 0
n = len(str(num))  # Number of digits

while num > 0:
    digit = num % 10
    sum_of_powers += digit ** n
    num = num // 10

if sum_of_powers == original_num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
    