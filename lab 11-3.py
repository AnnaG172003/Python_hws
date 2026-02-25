def is_primeNum(num):  
    for i in range(2, int(num**0.5)+1):
        if num % i == 0 :
            return False
    return True


num = int(input("Please input an integer: "))
if is_primeNum(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
