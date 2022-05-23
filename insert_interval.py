from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i_start, i_end = newInterval

        # find the index to insert the interval at
        idx = 0
        while idx < len(intervals):
            interval = intervals[idx]
            # the newInterval conflicts with the current interval
            if i_start <= interval[1]:
                break
            result.append(list(interval))
            idx += 1

        if idx == len(intervals):
            # no conflicts, the new interval belongs at the end
            result.append(newInterval)
        else:
            # insert in the middle of intervals
            # no conflict => no merge
            if i_end < intervals[idx][0]:
                result.append(newInterval)
                while idx < len(intervals):
                    result.append(list(intervals[idx]))
                    idx += 1

            # conflict => merge
            else:
                m_start, m_end = min(i_start, intervals[idx][0]), max(i_end, intervals[idx][1])
                while idx < len(intervals):
                    start, end = intervals[idx]
                    if m_end < start:
                        # done merging
                        break
                    else:
                        # merge
                        m_end = max(m_end, end)
                    idx += 1
                result.append([m_start, m_end])

                while idx < len(intervals):
                    result.append(intervals[idx])
                    idx += 1
        return result
