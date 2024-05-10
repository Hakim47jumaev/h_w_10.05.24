def find_odd(str1,s):
    for i in str1:
        if i in "aeyuoi":
            print(s,end="")
        else:
            print(i,end="")
find_odd("the number","#")