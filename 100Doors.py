doors = ["open" for i in range(100)]

for j in range(100):
    for i in range(j,len(doors),j+1):
        if doors[i] == "closed":
            doors[i] = "open"
        else:
            doors[i] = "closed"
print(doors)

