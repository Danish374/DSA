import collections
import bisect

class Packet:
    def __init__(self, source: int, destination: int, timestamp: int):
        self.source = source
        self.destination = destination
        self.timestamp = timestamp

    def __eq__(self, other):
        return (self.source == other.source and
                self.destination == other.destination and
                self.timestamp == other.timestamp)

    def __hash__(self):
        return hash((self.source, self.destination, self.timestamp))

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = collections.deque()
        self.unique = set()  # to check duplicates
        self.dest_times = collections.defaultdict(list)
        self.processed_index = collections.defaultdict(int)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        pkt = Packet(source, destination, timestamp)
        if pkt in self.unique:
            return False
        if len(self.queue) == self.memoryLimit:
            self.forwardPacket()
        self.queue.append(pkt)
        self.unique.add(pkt)
        self.dest_times[destination].append(timestamp)
        return True

    def forwardPacket(self) -> list[int]:
        if not self.queue:
            return []
        pkt = self.queue.popleft()
        self.unique.remove(pkt)
        self.processed_index[pkt.destination] += 1
        return [pkt.source, pkt.destination, pkt.timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        times = self.dest_times.get(destination, [])
        if not times:
            return 0
        start_idx = self.processed_index[destination]
        lo = bisect.bisect_left(times, startTime, lo=start_idx)
        hi = bisect.bisect_right(times, endTime, lo=start_idx)
        return hi - lo
