"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts, ends = [], []
        for interval in intervals:
            s, e = interval.start, interval.end
            starts.append(s)
            ends.append(e)
        starts.sort(reverse=True)
        ends.sort(reverse=True)

        count = 0
        res = 0
        while starts and ends:
            if starts[-1] < ends[-1]:
                starts.pop()
                count += 1
            elif starts[-1] == ends[-1]:
                ends.pop()
                starts.pop()
            else:
                ends.pop()
                count -= 1
            res = max(res, count)
        return res
