from collections import defaultdict, deque

class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        meetings.sort(key=lambda x: x[2])
        know = set([0, firstPerson])
        i = 0
        
        while i < len(meetings):
            time = meetings[i][2]
            graph = defaultdict(list)
            people = set()
            
            while i < len(meetings) and meetings[i][2] == time:
                a, b, _ = meetings[i]
                graph[a].append(b)
                graph[b].append(a)
                people.add(a)
                people.add(b)
                i += 1
            
            q = deque(p for p in people if p in know)
            seen = set(q)
            
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if v not in seen:
                        seen.add(v)
                        q.append(v)
            
            know |= seen
        
        return list(know)
