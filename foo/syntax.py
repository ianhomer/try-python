import random

# All the syntax
# Mostly from https://www.w3schools.com/python

print("syntax")

# Variables & data types

a = 1
b = "Hello"
c = str(3)
d = int("3")
e = float("3.5")
f = bool("true")
g = 123e10
h = """
Multi
Line
"""

print(f"{a}" + b + f"{c}{d * 2}{e}{f} {g}")
print(type(d))
print(h)
print("character:" + b[0] + str(len(b)))
for x in "hello":
    print(x)

assert b[3:5] == "lo"  # 5 non-inclusive
assert "llo" in b
assert "bye" not in b
assert b[::-1] == "olleH"
assert b[:3] == "Hel"
assert b[1:] == "ello"

if (
    1 == 1
    and 2 == 2
    and 3 == 3
    and 4 == 4
    and 5 == 5
    and 6 == 6
    and 7 == 7
    and 8 == 8
    and 9 == 9
):
    print("it is")

# Operators

assert 63 % 10 == 3
assert 63 // 10 == 6  # Floor division
assert 2**4 == 16
assert 4 & 3 == 0  # AND 100 & 011 == 0
assert 4 | 3 == 7  # OR 100 | 011 == 111
assert 4 ^ 7 == 3  # XOR 100 | 111 == 011
assert ~5 == -6  # NOT 00000101 == 111111010
assert 7 >> 1 == 3
assert 7 << 1 == 14

# Lists

my_list = ["a", "b", "c"]
assert len(my_list) == 3
assert len(list()) == 0  # empty list
assert my_list[1] == "b"
assert "b" in my_list
assert d not in my_list
my_list[0] = "aa"
assert my_list[0] == "aa"
my_list[0:2] = ["aaa", "bbb"]  # Replace range
print(my_list)
assert my_list == ["aaa", "bbb", "c"]
my_list[0:1] = ["aaa", "extra"]  # Insert array into position
assert my_list == ["aaa", "extra", "bbb", "c"]
my_list.insert(0, "first")
my_list.append("last")
my_list.extend(["1", "2", "3"])
my_list.remove("bbb")
print(my_list)
my_list.pop()  # pop the end
print(my_list)
my_list.pop(1)  # pop a given index
print(my_list)
del my_list[0]  # remove index
my_list.clear()

my_list = ["a", "b", "c"]
for x in my_list:
    pass
for i in range(len(my_list)):
    pass
i = 0
while i < len(my_list):
    i = i + 1
[print(x) for x in my_list]  # List comprehension
assert [x for x in my_list if x != "b"] == ["a", "c"]
assert [x for x in range(5)] == [0, 1, 2, 3, 4]
assert [x * 2 for x in range(5)] == [0, 2, 4, 6, 8]
my_list = ["a", "c", "b"]
my_list.sort()
assert my_list == ["a", "b", "c"]
my_list.sort(reverse=True)


def my_fun(_):
    return random.randint(0, 9)


my_list.sort(key=my_fun)
my_list.sort(key=str.lower)
my_list.reverse()

assert list(map(lambda x: x * 2, [1, 2])) == [2, 4]

# Tuples

my_tuple = (1, 2)

# Sets

my_set = {1, 2}

# Dictionary

my_dict = {"a": 1, "b": 2}
assert [x for x in my_dict] == ["a", "b"]
for x, y in my_dict.items():
    print(x, y)

# if

print("hello") if True else print("never")

# Lambda


def my_lambda(n):
    return lambda x: x * n


doubler = my_lambda(2)

print(doubler(4))

# Classes


class MyClass:
    def __init__(self, n: int):
        self.n = n


class MySuperClass(MyClass):
    def __init__(self, n, s: str):
        MyClass.__init__(self, n)
        self.s = s


object = MyClass(4)
object = MySuperClass(4, "hello")

# Iterators

my_tuble = (1, 2)
my_iterator = iter(my_tuple)
print(next(my_iterator))
print(next(my_iterator))

# Exception handling

try:
    i = 1 / 0
except Exception as error:
    print("No!", error)
