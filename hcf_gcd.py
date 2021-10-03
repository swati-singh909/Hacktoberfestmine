def compute_hcf(x, y):

    if x > y:  # Choosing the smaller number
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):  # Running for loop from 1 to smaller number + 1
        if((x % i == 0) and (y % i == 0)):  # If both the conditions satisfies the hcf is `i`
            hcf = i 
    return hcf


while True:
    num1 = abs(int(float(input("Enter 1st Number: \t")))) # Taking Input
    num2 = abs(int(float(input("Enter 2nd Number: \t")))) # Taking Input
    print(f"The H.C.F (GCD) of {num1} and {num2} is:\t {compute_hcf(num1, num2)}\n") # Printing the output
