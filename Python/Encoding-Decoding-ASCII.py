def encodeString(stringVal):
    enco = ""
    i = 0
    while i < len(stringVal):
        c = 1
        while i+1 < len(stringVal) and stringVal[i] == stringVal[i+1]:
            i += 1
            c += 1
        enco += str(c) + stringVal[i]
        i += 1
    return enco
def decodeString(encodedList):
    deco = ""
    i = 0
    while i < len(encodedList):
        c = int(encodedList[i])
        char = encodedList[i+1]
        deco += c*char
        i += 2
        return deco
m = encodeString("AAABBBAA")
dec = decodeString(m)
a = [(m[i + 1], int(m[i])) for i in range(0, len(m), 2)]
print(a)
print(dec)