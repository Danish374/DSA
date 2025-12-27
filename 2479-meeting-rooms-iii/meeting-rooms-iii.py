import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        free = list(range(n))
        heapq.heapify(free)
        busy = []
        count = [0] * n
        
        for start, end in meetings:
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(free, room)
            
            if free:
                room = heapq.heappop(free)
                heapq.heappush(busy, (end, room))
            else:
                t, room = heapq.heappop(busy)
                heapq.heappush(busy, (t + end - start, room))
            
            count[room] += 1
        
        return count.index(max(count))
