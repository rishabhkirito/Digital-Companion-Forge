def recursion(s):
    if len(s) <= 1:
        return s
    
    return recursion(s[1:]) + s[0]
   
print(recursion("hallauha"))
print(f"the reverse of hello is {recursion("hello")}")