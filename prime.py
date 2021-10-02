def is_prime(num):
    prime = None    # Creating an empty variable
    # If given number is greater than 1
    if num > 1:   
        # Iterate from 2 to n / 2  
        for i in range(2, num):  
            # If num is divisible by any number between  
            # 2 and n / 2, it is not prime
            if (num % i) == 0:   # If number is divisible by any number between 2 to num then its not prime
                prime = False   # Setting prime to false
                break
        else:
            prime = True  # Else setting prime to true
            pass

        if prime:  # Checking if the value of variable is True, if its True then its prime else not.SS
            print(f"{num} is a prime number.\n")
        else:
            print(f"{num} is not a prime number.\n")    

    else: 
        print(f"{num} is not a prime number.\n")


while True:
    num = abs(int(float(input("Enter A Number: \t"))))  # Taking input
    is_prime(num)   # Running the function
