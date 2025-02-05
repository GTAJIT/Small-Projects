class Solutoion:
    def twoSum(self, num:list[int], target: int) -> list[int]:
            for i in range(len(num)):
                for j in range(i+1,len(num)):
                    if num[i]+num[j] == target:
                        print([i,j])
a = [1,3,5,7,1]
b = 8
f = Solutoion()
f.twoSum(a, b)