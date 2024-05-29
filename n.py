class IdIterable:
    def __init__(self, objects):
        self.objects = objects
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.objects):
            obj = self.objects[self.index]
            self.index += 1
            return obj.id
        else:
            raise StopIteration()

class Person:
    def __init__(self, id, name, age, gender):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f"Person(id={self.id}, name='{self.name}', age={self.age}, gender='{self.gender}')"

persons = [
    Person(1, "John Doe", 35, "Male"),
    Person(2, "Jane Smith", 28, "Female"),
    Person(3, "Bob Johnson", 42, "Male"),
    Person(4, "Sarah Lee", 31, "Female")
]

for person_id in IdIterable(persons):
    print(person_id)
