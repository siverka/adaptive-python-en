class Buffer:
    def __init__(self):
        self.elements = []

    def add(self, *a):
        self.elements.extend(a)
        while len(self.elements) >= 5:
            print(sum(self.elements[:5]))
            self.elements = self.elements[5:]

    def get_current_part(self):
        return self.elements


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()  # return [1, 2, 3]
buf.add(4, 5, 6)  # print(15) – output of the sum of the first five elements
buf.get_current_part()  # return [6]
buf.add(7, 8, 9, 10)  # print(40) – output the sum of the second five elements
buf.get_current_part()  # return []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – output the sum of the third and fourth five elements
buf.get_current_part()  # return [1]
