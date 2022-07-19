##from dataclasses import dataclass


@dataclass(order= True)
class person:
    name: str
    age: int
    def is_minor(self):
        return self.age < 30

person1 = person("adeola", 3)
person2 = person("adeola", 34)

print(person1.age < person2.age)


from datetime import datetime, timedelta
d1 = datetime.now()
d2 = datetime(2021, 5, 27)
diff = d1 - d2
print(diff)

t = timedelta(weeks=-1)
print(d1 + t)

date_from_str = datetime.strptime("2022-02-02", "%Y-%m-%d")
print(date_from_str.year)

for lst in [1, 2, 3, 4, 5]:
    print(lst)

def custom_for(iterable, func):
    it = iter(iteratle)

    while True:
        try:
            func(next(it))
        except StopIteration:
            break

def cube(num):
    print(num ** 3)


custom_for([1, 2, 3, 4,5], cube)



def gen ():
    counter = 0
    while True:
        yield counter
        count += 1

tiger = gen()
print(next(tiger))
print(next(tiger))##





