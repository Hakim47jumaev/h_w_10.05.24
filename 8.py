def stupid_addition(a,b):
    if type(a) is type(b):
        try:
            if float(a):
                return a+b
        except:
            return a+b
    else:
        return None

print(stupid_addition("1","3"))