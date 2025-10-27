class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        prev = 0
        total = 0

        for row in bank:
            devices = row.count('1')
            if devices:
                total += prev * devices
                prev = devices

        return total
