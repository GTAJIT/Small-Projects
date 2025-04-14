#linkdin project
def fac(n):
        if type(n)==int and n == 0:
            return 1
        elif type(n) == int and n>0:
            return n*fac(n-1)
        else:
            return None
n = -5
print(f"The Factorial pf {n} is {fac(n)}")