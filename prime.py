def prime(n=100):
    r=[]
    for i in range(2,n+1):
        f=0
        for j in range(2,i):
            if i%j==0:
                f+=1
        if( f==0):
            r.append(i)
    return r

print(prime(int(input ("Enter number: "))))
print(f"By defalut list of prime number between 0 to 100 : {prime()}")