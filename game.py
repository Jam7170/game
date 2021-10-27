version = "0.0.1"


#global variables
day = 1
gold = 10
goldPerday = 1
hasJob = True
wage = 20

#shop variables
class shop:
    bonus = 0
    price_coffee = 0

def progressDay():
    global day
    global gold
    day += 1
    #gold += goldPerday
    shop.bonus = 0
    print("Day: " + str(day))
    checkWallet()
def openShop():
    global gold
    global wage
    isShopOpen = True
    with open('shop.txt', 'r') as reader:
        print(reader.read())
    while isShopOpen == True:
        buy = (input("Buy>"))
        match buy:
            case "coffee":
                if gold >= shop.price_coffee:
                    print("* You purchased a coffee")
                    gold -= shop.price_coffee
                    shop.bonus += 10
                else: print("You have insufficent funds.")
            case "exit":
                isShopOpen = False
    #exec(open("shop.py").read())
def checkWallet():
    print("Money: " + str(gold))
def work():
    global gold
    if hasJob == True:
        print("You spent the day at work.")
        pay = wage + shop.bonus
        print(pay)
        gold += pay
        progressDay()
    else: print("You don't have a job.")


print("Day: " + str(day))
checkWallet()
#Main loop
while True:
    action = (input(">"))
    
    match action:
        case "wallet":
            checkWallet()
        case "shop":
            openShop()
        case "work":
            work()
        case"dev_checkbonus":
            print("Bonus: " + str(shop.bonus))
        case "sleep":
            progressDay()