print("<--------------------HCF FINDER------------------->")
a=int(input("Enter first nummber :"))
b=int(input("Enter second number : "))
print("=====================SOLUTION=====================")
while 1:
    q=a//b
    r=a%b

    print(str(a)+"="+str(b)+"X"+str(q)+"+"+str(r))

    if not r:
        break
    a=b
    b=r
print("==================================================")
print('HCF is:', b)
