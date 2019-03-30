
lucky_numbers =[4,8,10,12,24,8,10]
friends = ["kevin","bob","Béla",10,True]

friends.append("Creed")
friends.insert(2, "Kelly")
friends2 = friends.copy()
friends.remove("kevin")
friends.pop()
friends[3]="Mike"

lucky_numbers.sort()
lucky_numbers.reverse()

friends.extend(lucky_numbers)


print(friends)
print(friends[6])
print(friends[1:3])
print(friends.index("bob"))
print(friends.count(8))
print(friends)
print(lucky_numbers)
print(friends2)