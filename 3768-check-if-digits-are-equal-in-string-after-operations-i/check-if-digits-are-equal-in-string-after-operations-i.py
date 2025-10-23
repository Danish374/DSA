class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(ch) for ch in s]
        n = len(digits)
        while len(digits) > 2:
            new = [(digits[i] + digits[i+1]) % 10 for i in range(len(digits)-1)]
            digits = new
        return digits[0] == digits[1]
