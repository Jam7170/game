import random

version = "0.0.1"

day = 1
gold = float(10)
goldPerday = 1
hasJob = True
wage = float(20)
bonus = float(0)

class Item:
    def __init__(this, name, price, buff):
        this.name = name
        this.price = price
        this.buff = buff
    
itmCoffee = Item("Coffee", 3, 5)
itmTest = Item("Test", 1, 15)

class Skill:
    skillList = []
    level = 0
    def __init__(this, name):
        this.name = name
        Skill.skillList.append(this.name)
        
    def lvlup(this, amount, message=None):
        this.level += amount
        if message == True:
            print("\"{}\" skill increased!".format(this.name))
        
sklCooking = Skill("Cooking")
sklDance = Skill("Dance")

def progressDay():
    global day
    global gold
    day += 1
    gold += goldPerday
    bonus = 0
    print("Day: " + str(day))
    checkWallet()
def openShop():
    global gold; global wage; global bonus
    isShopOpen = True
    # with open('shop.txt', 'r') as reader:
    #     print(reader.read())
    while isShopOpen == True:
        buy = (input("Buy>"))
        match buy:
            case "coffee":
                buyItem(itmCoffee)
            case "test":
                buyItem(itmTest)
            case "exit":
                isShopOpen = False
    #exec(open("shop.py").read())
def buyItem(item):
    global gold; global bonus
    if gold >= item.price:
        print("* You purchased a {}".format(item.name))
        gold -= item.price
        bonus += item.buff/100
    else: print("You have insufficent funds.")
def checkWallet():
    print("Money: " + str(gold))
def work():
    global gold
    if hasJob == True:
        print("You spent the day at work.")
        pay = wage * (bonus+1)
        print(pay)
        gold += pay
        progressDay()
    else: print("You don't have a job.")
def cook():
    lowCookingDialouge = ["* lowCookingDialouge1", "* lowCookingDialouge2", "* lowCookingDialouge3"]
    medCookingDialouge = ["* medCookingDialouge1", "* medCookingDialouge2", "* medCookingDialouge3"]
    highCookingDialouge = ["* highCookingDialouge1", "* highCookingDialouge2", "* highCookingDialouge3"]
    if sklCooking.level < 5: print(random.choice(lowCookingDialouge))
    elif sklCooking.level < 8 and sklCooking.level > 4 : print(random.choice(medCookingDialouge))
    else: print(random.choice(highCookingDialouge))

def main():
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
            case "cook":
                cook()
            case "sleep":
                progressDay()
                
            case "quit":
                return False
                
            case "dev_checkbonus":
                print("Bonus: " + str(bonus))
            case "skilltest":
                sklCooking.lvlup(1, True)
                print(sklCooking.level)
                
if __name__ == "__main__": main()
else: print("Imported " + __name__)