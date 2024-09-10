def oddeven(a):
    if(a%2==0):
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a Number: "))
print("The Given Number is", oddeven(num))
