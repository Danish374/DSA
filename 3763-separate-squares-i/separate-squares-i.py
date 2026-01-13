class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        def area_above(mid):
            area = 0
            for _, y, l in squares:
                top = y + l
                if top > mid:
                    area += l * max(0, top - max(y, mid))
            return area

        total = sum(l * l for _, _, l in squares)
        half = total / 2

        for _ in range(60):
            mid = (low + high) / 2
            if area_above(mid) > half:
                low = mid
            else:
                high = mid
        return low
