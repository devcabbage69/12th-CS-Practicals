odd = set(range(1, 10, 2))
prime = set()

for i in range(2, 10):
    for j in range(2,i):
        if(i%j == 0):
            break
        else:
            prime.add(i)

print("Odd Number: ", odd)
print("Prime Number: ", prime)
print("Union: ", odd.union(prime))
print("Intersection: ", odd.intersection(prime))
print("Difference: ", odd.difference(prime))
print("Symmetric Difference: ", odd.symmetric_difference(prime))
