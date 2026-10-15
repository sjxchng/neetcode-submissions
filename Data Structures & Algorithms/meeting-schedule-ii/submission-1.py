"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        for interval in intervals:
            start, end = interval.start, interval.end
            starts.append(start)
            ends.append(end)
        starts.sort(reverse=True)
        ends.sort(reverse=True)
        
        res = 0
        cur_rooms = 0
        while starts:
            if starts[-1] < ends[-1]:
                cur_rooms += 1
                starts.pop()
            else:
                cur_rooms -= 1
                ends.pop()
            res = max(res, cur_rooms)
        return res