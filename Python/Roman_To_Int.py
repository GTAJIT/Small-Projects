class Solution:
    def romanToInt(self, s: str) -> int:
        val = {
            "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000
        }
        total = 0
        value = 0
        try:
            for i in reversed(s):
                current_val = val[i]
                if current_val < value:
                    total -= current_val
                else:
                    total += current_val
                value = current_val
            return total
        except Exception as e:
            return(f"Unexpected Error {e}")
solution = Solution()
x = input("Enter The Roman Letter: ")
a = len(x)
if 1<=a<=15:
    y = x
else: 
    print(f"it dont fit the criteria [1<={a}<=15]")
result = solution.romanToInt(y.upper())
print(result)