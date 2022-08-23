class TimeMap:

    def __init__(self):
        self.dict = {}  # key -> (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        return self.binary_search(self.dict[key], timestamp)

    def binary_search(self, values: List[Tuple[int, str]], timestamp: int) -> str:
        l, r = 0, len(values) - 1
        prospect = -1
        while l <= r:
            m = l + (r - l) // 2
            if values[m][0] == timestamp:
                return values[m][1]
            elif values[m][0] < timestamp:
                prospect = m
                l = m + 1
            else:
                r = m - 1
        if prospect == -1:
            return ""
        return values[prospect][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# will use the bisect module provided by Python
