t1 = int(input())
t2 = int(input())
t3 = int(input())
podium = {"gold": "", "silver": "", "bronze":""}

if (t1 < t2) and (t1 < t3):
    podium["gold"] = 1
    if (t2 < t3):
        podium["silver"] = 2
        podium["bronze"] = 3
    else:
        podium["silver"] = 3
        podium["bronze"] = 2
elif t2 < t1 and t2 < t3:
    podium["gold"] = 2
    if (t1 < t3):
        podium["silver"] = 1
        podium["bronze"] = 3
    else:
        podium["silver"] = 3
        podium["bronze"] = 1
elif t3 < t1 and t3 < t2:
    podium["gold"] = 3
    if (t1 < t2):
        podium["silver"] = 1
        podium["bronze"] = 2
    else:
        podium["silver"] = 1
        podium["bronze"] = 2

print(podium["gold"])
print(podium["silver"])
print(podium["bronze"])
