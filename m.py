class MyCollection:
    objects = []

    def __init__(self, value):
        self.value = value
        MyCollection.objects.append(self)
    
    def __iter__(self):
        return MyCollectionIterator(MyCollection.objects)

    def __repr__(self):
        return f"MyCollection(value={self.value})"

class MyCollectionIterator:
    def __init__(self, objects):
        self._objects = objects
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._objects):
            result = self._objects[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

obj1 = MyCollection(1)
obj2 = MyCollection(2)
obj3 = MyCollection(3)

for obj in MyCollection.objects:
    print(obj)