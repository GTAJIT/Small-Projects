import random
import string
s = input("Enter Letter: ")
c = "Code"
d = "Decode"
print(f"a. {c} ",f"b. {d}")
j = input("What you want to do: ").lower()
if j=="a":
    m = c
elif j=="b":
    m = d
else:
    print("Invalid Selection! ")
def code_worker(letters):
    if j=="a":
        if len(s)>=3:
            #gen part!
            def gen_random_word(length):
                letter = string.ascii_lowercase
                return ''.join(random.choice(letter)for _ in range(length))
            a = gen_random_word(3)
            b = gen_random_word(3)
            #append part!
            k = s[1:] + s[0]

            ans = a+k+b
        else:
            ans = s[::-1]
    elif j=="b":
        if len(s)<3:
            ans = s[::-1]
        else:
            l = len(s)-4
            ans = s[l]+s[3:l]
    print (f"Your letter  {s}  After {m}ing is: {ans}")
code_worker(s)