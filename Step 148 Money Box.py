class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0

    def can_add(self, v):
        return v + self.count <= self.capacity

    def add(self, v):
        self.count += v
