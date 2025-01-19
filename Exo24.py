def nbOccurenceCharInList(c , lst):
    nb = 0
    for i in lst :
        if i == c :
            nb += 1
    return nb

def anagrams(s1 , s2):
    if len(s1) != len(s2) :
        return False
    
    for i in s1 :
        if nbOccurenceCharInList(i,s1) != nbOccurenceCharInList(i,s2) :
            return False
    
    return True

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if anagrams(s1 , s2):
    print(f"{s1} and {s2} are anagrams.")
else:
    print(f"{s1} and {s2} are not anagrams.")