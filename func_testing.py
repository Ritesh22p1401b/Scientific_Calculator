

# def permutation(n,r):
#     def fac(q):
#         c=1
#         while(q>=1):
#             c=c*q
#             q-=1
#         return c
#     s=n-r
#     result=fac(n) // fac(s)
#     return result


# num1=6
# num2=1
# print(permutation(num2,num1)




def fac(num):
    if num==1 or num==0:
        return 1
    
    return num*fac(num-1)


num=5
answer=fac(num)
print(answer)
