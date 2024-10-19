

def permutation(n,r):
    def fac(q):
        c=1
        while(q>=1):
            c=c*q
            q-=1
        return c
    s=n-r
    result=fac(n) // fac(s)
    return result


num1=6
num2=1
print(permutation(num2,num1))

