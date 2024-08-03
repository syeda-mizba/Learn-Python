try:
    n1 = int(input("Enter the starting range: "))
    n2 = int(input("Enter the ending range: "))
except ValueError:
    print("Invalid input. Please enter integer values.")
    exit()
    
if n1 < 2:
    print("Starting number should be greater than or equal to 2.")
elif n2 < 2:
    print("Ending number should be greater than or equal to 2.")
elif n1 > n2:
    print("Starting number should be less than or equal to ending number.")
else:
    
prime_numbers = []

    for num in range(n1, n2 + 1):  
        for i in range(2, num):  
            if (num % i) == 0:
                break  
        else:
            prime_numbers.append(num)  

    if prime_numbers:
        print(f"The prime numbers from the range {n1} to {n2} are: {', '.join(map(str, prime_numbers))}")
    else:
        print(f"There are no prime numbers in the range {n1} to {n2}.")
