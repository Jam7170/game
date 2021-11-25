from os import sep
import random
from skills import *
from items import *


version = "0.0.1"
dev_mode = True

day = 1
money = 10
daily_money = 1
has_job = True
wage = 20
bonus = 0

def progressDay():
    global day, money, bonus
    day += 1
    money += daily_money
    bonus = 0
    print("Day: " + str(day))
    checkWallet()
def checkWallet():
    print("Money: " + str(money))
def openShop():
    global money; global wage; global bonus
    isShopOpen = True
    with open('shop.txt', 'r') as reader:
        print(reader.read())
    while isShopOpen:
        buy = (input("Buy>"))
        buy = buy.lower()
        if buy == "coffee":
                buyItem(itmCoffee)
        elif buy == "test":
                buyItem(itmTest)
                
        elif buy == 'wallet':
                checkWallet()
        elif buy == "exit":
                isShopOpen = False
        else: continue
def buyItem(item):
    global money; global bonus
    if money >= item.price:
        print(f'* You purchased a {item.name}')
        money -= item.price
        bonus += item.buff/100
    else: print('You have insufficent funds.')
def work():
    global money
    if has_job == True:
        print("You spent the day at work.")
        pay = wage * (bonus+1)
        print(pay)
        money += pay
        progressDay()
    else: print("You don't have a job.")
def cook():
    lowCookingDialouge = ["* lowCookingDialouge1", "* lowCookingDialouge2", "* lowCookingDialouge3"]
    medCookingDialouge = ["* medCookingDialouge1", "* medCookingDialouge2", "* medCookingDialouge3"]
    highCookingDialouge = ["* highCookingDialouge1", "* highCookingDialouge2", "* highCookingDialouge3"]
    if sklCooking.level < 5: print(random.choice(lowCookingDialouge))
    elif sklCooking.level < 8 and sklCooking.level > 4 : print(random.choice(medCookingDialouge))
    else: print(random.choice(highCookingDialouge))
    if random.randint(0,10) <= 3:
        sklCooking.lvlup(1, True)

def main():
    print("Day: " + str(day))
    checkWallet()
    #Main loop
    while True:
        action = (input("> "))
        if action.startswith("dev_") and not dev_mode: continue
        
        if action == "wallet":
                checkWallet()
        elif action == "shop":
                openShop()
        elif action ==  "work":
                work()
        elif 'cook':
                cook()
        elif "sleep":
                progressDay()
                
        elif "quit"|'exit'|'q'|'e':
                break
                
        elif "dev_bonus":
                print("Bonus: " + str(bonus))
        elif "dev_skilltest":
                sklCooking.lvlup(1, True)
                print(f'Cooking Skill: {sklCooking.level}')
                
        else:
            print("Invalid Action")
                
if __name__ == "__main__": main()
else: print("Imported " + __name__)