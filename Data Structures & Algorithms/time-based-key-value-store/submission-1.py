class TimeMap:

    def __init__(self):
        self.key_to_timestamped_values = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_timestamped_values[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.key_to_timestamped_values.get(key, [])
        left, right = 0, len(values)

        if not values:
            return ""

        while left < right: 
            mid = (left + right) // 2
            if values[mid][0] > timestamp:
                right = mid
            else:
                left = mid + 1

        if left == 0:
            return ""        
        
        return values[left - 1][1]

