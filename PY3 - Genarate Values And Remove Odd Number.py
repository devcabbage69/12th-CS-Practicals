num = list(range(1,11))
print("Number From 1 to 10... \n", num)

for i in num:
    if(i%2 == 1):
        num.remove(i)
print("The Values After Removing Odd Numbers: \n", num)
