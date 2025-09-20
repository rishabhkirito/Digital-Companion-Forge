def recursion(s):
    if len(s) <= 1:
        return s
    
    return (s[1:]) + s[0]
   
recursion_word = input("enter a word: ")
if recursion_word == exit:
    exit
print(recursion(recursion_word))