a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))
d = int(input("Enter value of d: "))

if(a>b and a>c and a>d):
    print("a is greater number")
elif(b>a and b>c and b>d):
    print("b is greater number")
elif(c>a and c>b and c>d):
    print("c is greater number")
else:
    print("d is greater number")