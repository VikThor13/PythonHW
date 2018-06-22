import sys

digit_str = sys.argv[1]
summ = 0
for num in digit_str:
    summ += int(num)
print(summ)