class Solution:
    def getNoZeroIntegers(self, n: int):
        def hasZero(num: int) -> bool:
            return '0' in str(num)
        
        for a in range(1, n):
            b = n - a
            if not hasZero(a) and not hasZero(b):
                return [a, b]
        return []
