def valid(a):
    if len(a)==4 or len(a)==6:
        for i in a:
            if i not in "1234567890":
                return False
        else:
            return True
            
    else:
        return False
a=input()
print(valid(a))