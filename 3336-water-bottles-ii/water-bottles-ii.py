class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = 0
        full = numBottles
        empty = 0

        while full > 0:
            total += full
            empty += full
            full = 0

            if empty >= numExchange:
                full = 1
                empty -= numExchange
                numExchange += 1

        return total
