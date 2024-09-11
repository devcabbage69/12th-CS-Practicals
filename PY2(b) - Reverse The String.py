def reverse(str1):
    str2 = ''
    for i in str1:
        str2 += i
        return str2
word = input("Enter a String: ")
print("The Reverse of The String is: ", reverse(word))
