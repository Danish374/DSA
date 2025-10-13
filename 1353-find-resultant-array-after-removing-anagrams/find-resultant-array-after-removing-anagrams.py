from collections import Counter

class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        def is_anagram(a: str, b: str) -> bool:
            if len(a) != len(b):
                return False
            cnt = Counter(a)
            for c in b:
                cnt[c] -= 1
                if cnt[c] < 0:
                    return False
            return True
        
        result = []
        for w in words:
            if not result or not is_anagram(result[-1], w):
                result.append(w)
        return result
