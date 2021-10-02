out = [] # Initialising an empty list which will store out results
def table(num, start=1): # Table function which will return us a list of numbers as table of the given number
    global upto
    if start > upto: # Code logic
        return
    out.append(str(num * start))

    return table(num, start + 1)

while True:
    num = int(input("Enter a number to print out its table:\t"))
    upto = int(input("Enter number upto where you want to print table:\t"))
    table(num, 1)
    print(", ".join(out), "\n")
    out = []
