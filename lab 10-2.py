while True:
    num = int(input("Please input k: "))
    if num <= 0:
        print("Please enter a positive number!")
        continue
    if num < 2:
        print(num, "is not a prime number.")
        continue
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number.")
            break
    else:
        break
primes = []
next_num = 2
while len(primes) < num:
    for i in range(2, int(next_num ** 0.5) + 1):
        if next_num % i == 0:
            break
    else:
        primes.append(next_num)
    next_num += 1
print(" Prime numbers:", primes)