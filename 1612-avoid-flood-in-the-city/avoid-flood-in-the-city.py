from typing import List
import bisect

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        full = {}
        dry_days = []
        for i, lake in enumerate(rains):
            if lake > 0:
                if lake in full:
                    j = bisect.bisect_right(dry_days, full[lake])
                    if j == len(dry_days):
                        return []
                    ans[dry_days[j]] = lake
                    dry_days.pop(j)
                full[lake] = i
                ans[i] = -1
            else:
                dry_days.append(i)
                ans[i] = 1

        return ans
