# All the syntax

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
