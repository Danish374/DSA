class Solution:
    def countCollisions(self, directions: str) -> int:
        s = directions.lstrip('L').rstrip('R')
        if not s:
            return 0
        return len(s) - s.count('S')
