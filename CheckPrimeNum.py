n = int(input("Enter a number: "))  # get input from the user
if n == 1:
    print(n, "is not a prime number.")  # 1 is not considered a prime number
elif n > 1:
    # loop from 2 to n-1 to check for divisors
    for i in range(2, n):
        if (n % i) == 0:
            # if n is divisible by i, it is not a prime number
            print(n, "is not a prime number.")
            break  # Exit the loop since we found a divisor
    else:
        # if the loop completes without finding a divisor, n is a prime number
        print(n, "is a prime number.")


    

