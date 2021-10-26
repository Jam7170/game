version = "0.0.1"

day = 1
gold = float(10)
goldPerday = float(1)
hasJob = True
wage = float(20)
bonus = 0

def progressDay():
    global day
    global gold
    day += 1
    gold += goldPerday
    bonus = 0
    print("Day: " + str(day))
    checkWallet()
def openShop():
    global bonus
    global gold
    global wage
    isShopOpen = True
    with open('shop.txt', 'r') as reader:
        print(reader.read())
    while isShopOpen == True:
        buy = (input("Buy>"))
        match buy:
            case "coffee":
                if gold >= 3:
                    print("* You purchased a coffee")
                    gold -= 3
                    bonus += 5
                else: print("You have insufficent funds.")
            case "exit":
                isShopOpen = False
    #exec(open("shop.py").read())
def checkWallet():
    print("Money: " + str(gold))
    
print("Day: " + str(day))
checkWallet()
while True:
    action = (input(">"))
    
    match action:
        case "wallet":
            checkWallet()
        case "shop":
            openShop()
        case "work":
            if hasJob == True:
                print("You spent the day at work.")
                gold += (wage + (bonus/100) * wage)
                progressDay()
            else: print("You don't have a job.")
        case "sleep":
            progressDay()