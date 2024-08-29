p = 3
q = 11
n = p*q
a = (p-1)*(q-1)
e = int(input("Value of E: "))
if 1<e<a:
    d = round((1*a)/e)
    print("Public Key: ",(e,n))
    print("Private Key: ",(d,n))
    m = (2**e)%n
    c = (29**d)%n
    print("The Encryption of M: ",m)
    print("The Decryption of C: ",c)
else:
    print("Give a Correct Value (1<E<{a})")