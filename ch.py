a=("chan","good")
x=list(a)
x[1]="man"
a=x
print(a)

print(type(a))


b=int(input())
c=int(input())
d=int(input("d is greater:"))

if b>c and b>d:
    print("b is greater:"+b)
if c>b and c>d:
    print("c is greater:"+c)
else:
    print(d)
