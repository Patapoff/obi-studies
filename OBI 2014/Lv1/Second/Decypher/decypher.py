sequence = list([char for char in input()])
dic = {}
str = ""

for i in range(0, len(sequence)):
    dic[chr(97+i)] = sequence[i]

for charac in input():
    str += dic[charac]

print(str)
