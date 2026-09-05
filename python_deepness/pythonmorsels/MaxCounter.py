from collections import Counter


class MaxCounter(Counter):

    def max_keys(self) -> list:
        data = [d for d in self.items() if d[1] > 0]

        if not data:
            return []

        max_key, max_val = max(data, key=lambda x: x[1])

        return [d[0] for d in data if d[1] >= max_val]
