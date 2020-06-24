# # For Loop -----------------------------------
Employee_list = ["Rabby", "Royel", "Basir"]
for x in Employee_list:
    print(x)

# # Break loop ---------------------------------
Employee_list = ["Rabby", "Royel", "Basir"]
for x in Employee_list:
    print(x)
    if x == "Royel":
        break

# # The range function --------------------------
for x in range(6):
    print(x)
for x in range(2, 30, 3):
    print(x)

# # Nested loop ---------------------------------
Color = ["red", "green", "blue"]
Branch_list = ["Bogskf", "Rngskf", "Frdskf"]

for x in Branch_list:
    for y in Color:
        print(x, y)
