from collections import namedtuple
Student = namedtuple('Student',['name','age', 'grade'])
s = Student('Alice', 20, 'A')
print(s.name,s.age,s.grade)
print(s)