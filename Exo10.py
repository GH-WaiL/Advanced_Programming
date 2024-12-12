word = input ("word : ")

i = 0
j = -1
m = len(word) // 2
while i <= m :
    if word[i] != word[j] :
        print("No, it's not a palindrome.")
        exit
    i += 1
    j -= 1
print("Yes, it's a palindrome.")
