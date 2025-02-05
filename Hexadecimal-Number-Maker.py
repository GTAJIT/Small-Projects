hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def hexToDec(hexNum):
    hexNum = hexNum.upper()
    for char in hexNum:
        if char not in hexNumbers:
            return f"Error: '{char}' is not a valid hexadecimal character!"
    
    decimal_value = 0
    hex_len = len(hexNum)
    for i, char in enumerate(hexNum):
        decimal_value += hexNumbers[char] * (16 ** (hex_len - i - 1))
    
    return decimal_value

# Get user input
a = input("HexNum: ")
# Convert hex to decimal and print the result
result = hexToDec(a)
print(result)


# hexnum = 342
# dec = 0
# len= len(hexnum) - 1
# for char in hexnum:
#     dec = dec + (hexnum[0]* (16**len))
#     len = len - 1
# return dec