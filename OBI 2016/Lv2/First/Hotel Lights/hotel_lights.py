input = list(input().split())
state = {"Ia": int(input[0]), "Ib": int(input[1]), "Fa":int(input[2]), "Fb":int(input[3])}

if state["Ia"]  == state["Fa"]:
    if state["Ib"] == state["Fb"]:
        print("0")
    else:
        print("2")
else:
    print("1")
