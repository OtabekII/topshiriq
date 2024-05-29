class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        self.current = self.start  
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration 
        else:
            current = self.current
            self.current += 1
            return current

my_range = MyRange(1, 5)

for num in my_range:
    print(num)