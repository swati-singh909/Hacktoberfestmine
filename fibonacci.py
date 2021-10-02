nterms = int(input("Enter number of terms:\t"))

# First two terms
n1, n2 = 0, 1
count = 0

fibo_int = []  # As numbers will be stored in int here

print("Fibonacci Series Upto 10 Terms:", end="\t\t")
while count < nterms:
   fibo_int.append(n1)
   nth = n1 + n2
   # update values
   n1 = n2
   n2 = nth
   count += 1

fibonacci_series = []  # Converting int to str because `"".join()` uses str instead of int

for item in fibo_int:
   item = str(item)
   fibonacci_series.append(item)

print(", ".join(fibonacci_series))
