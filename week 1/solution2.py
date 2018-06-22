import sys

n = int(sys.argv[1])
for i in range(1, n + 1):
    str = ''
    for j in range(1, n - i + 1):
        str += ' '
    for j in range(1, i + 1):
        str += '#'
    print(str)
