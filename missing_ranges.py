class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def format(lower: int, upper: int) -> str:
            if lower == upper:
                return str(lower)
            return str(lower)+'->'+str(upper)

        ranges = []
        if not nums:
            return [format(lower, upper)]

        # beginning missing
        if nums[0] != lower:
            ranges.append(format(lower, nums[0] - 1))

        # middle ranges
        prev = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            if curr != prev + 1:
                ranges.append(format(prev + 1, curr - 1))
            prev = curr

        # end missing
        if nums[-1] != upper:
            ranges.append(format(nums[-1] + 1, upper))

        return ranges
