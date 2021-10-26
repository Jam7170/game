shopopen = 1
bonus = 0
with open('shop.txt', 'r') as reader:
    print(reader.read())
while shopopen == 1:
    action = (input("Shop>"))
    match action:
        case "coffee":
            print("Placement Text")
            bonus = 5
        case "exit":
            shopopen = 0
