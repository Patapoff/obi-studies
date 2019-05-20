sticks = input().split()
sticks = list(map(int, sticks))
sticks.sort()
sticks = sticks[::-1]
possible = False

for i in range(0,2):
    if(sticks[i] < sticks[i+1]+sticks[i+2]):
        possible = True

if (possible):
    print("S")
else:
    print("N")
