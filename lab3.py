n = 33
series = raw_input("Please enter the string - ")
if series == "fibonacci":
    a, b = 0,1
    for i in range(n-1):
        a,b = b, a+b
        print a
elif series == "sum":
    i = 0
    a = 0
    while i < (3*n):
        x = 3
        i =+ (i+x)
        a = i + a
        print a
else:
    print "Invalid String!"