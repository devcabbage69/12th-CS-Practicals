n = int(input("Enter a value of n: "))
s = 0

for i in range(1, n+1):
    a = (i**i)/i
    s = s+a
print("The Sum of the series is ", s)
