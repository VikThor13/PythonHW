import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
d = b*b - 4*a*c
x1 = (-b + d**0.5) / (2 * a)
x2 = (-b - d**0.5) / (2 * a)
print(f"root1 = {int(x1):d}")
print(f"root2 = {int(x2):d}")
