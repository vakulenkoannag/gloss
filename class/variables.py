import re

s = """
a = 1
b = 4.545
c = .345
d = -24
G = 2*pi*a
"""

variables = re.findall(
#    r'^[a-zA-Z]+\s*=\s*-?\d+(?:\.\d+)?$',
    r'^(\w+)\s*=\s*(-?\d+(?:\.\d+)?)$',
    s,
    re.MULTILINE
)
print(variables)


# flag ^$ re.MULTILINE
