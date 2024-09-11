def reverse(str1):
    str2 = ''
    for i in str1:
        str2 = i + str2
    return str2
word = input("\n Enter a String: ")
print("\n The Reverse of The String is: ", reverse(word))
