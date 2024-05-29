class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, gender='{self.gender}')"

    def __iter__(self):
        return PersonIterator(self)

class PersonIterator:
    def __init__(self, person):
        self.person = person
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            self.index += 1
            return self.person
        else:
            raise StopIteration()

persons = [
    Person("John Doe", 35, "Male"),
    Person("Jane Smith", 28, "Female"),
    Person("Bob Johnson", 42, "Male"),
    Person("Sarah Lee", 31, "Female")
]

for person in persons:
    print(person)

print("---")

adult_persons = [p for p in persons if p.age > 30]
for person in adult_persons:
    print(person)

print("---")

male_persons = [p for p in persons if p.gender == "Male"]
for person in male_persons:
    print(person)

print("---")

female_persons = [p for p in persons if p.gender == "Female"]
for person in female_persons:
    print(person)