class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        langs = [set(l) for l in languages]

        need = set()
        for u, v in friendships:
            u, v = u - 1, v - 1
            if langs[u].intersection(langs[v]):
                continue
            need.add(u)
            need.add(v)

        if not need:
            return 0

        count = [0] * (n + 1)
        for person in need:
            for lang in langs[person]:
                count[lang] += 1

        return len(need) - max(count)
