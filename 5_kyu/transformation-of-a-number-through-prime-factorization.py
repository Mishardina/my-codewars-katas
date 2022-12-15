#https://www.codewars.com/kata/572caa2672a38ba648001dcd

def f(n):
    m,p=1,2
    while p*p<=n:
        k=0
        while n%p==0:
            k+=1
            n//=p
        if k:
            m*=k*p**(k-1)
        p+=1
    return m