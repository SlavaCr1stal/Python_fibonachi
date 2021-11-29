from random import randint
# Fib(n+2) = Fib(n+1) + Fib(n) -> Fib(m), m = n + 2, n = m - 2 -> Fib(m) = Fib(m-1) + Fib(m-2)
def Fibb (n):
    F1 = 1
    F2 = 1
    Fn = 1
    i = 3
    while i <= n:
        Fn = F1 + F2
        F1 = F2
        F2 = Fn
        i = i + 1
    '''while n !=1 or n!=2:
        Fn = F1 + F2
        F1 = F2
        F2 = Fn
        n = n - 1
    '''
    return Fn

def Fibb_r_1 (n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibb_r_1(n-1) + Fibb_r_1(n-2)
def Fibb_r_2 (n, F2 = 1, F1 = 1):
    if n == 1 or n == 2:
        return F2
    else:
        return Fibb_r_2(n-1, F2 = F1 + F2 ,F1 = F2)
print(Fibb(90))
print(Fibb_r_2(90))