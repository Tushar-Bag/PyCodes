
a=int(input("Take the first number: "))
b=int(input("Take the second number: "))
op=input("Chose the operation: ")

d=[]
for c in op:
    if c=="+":
        d=a+b
    if c =="-":
        d=a-b
    if c == "*":
       d=a*b
    if c =="/":
        d=a/b
print(d)

