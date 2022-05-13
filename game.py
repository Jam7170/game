import random
from skills import sklCooking
from items import Item
from dialogue import dialogue, dialogue_ellipsis, dialogue_input, clear

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
    dialogue("Day: " + str(day))
    checkWallet()

def checkWallet():
    dialogue("Money: " + str(money))

def openShop():
    global money, wage, bonus
    isShopOpen = True
    with open('shop.txt', 'r') as reader:
        print(reader.read())
    while isShopOpen:
        buy = (input("Buy>"))
        buy = buy.lower()
        if buy in Item.itemList:
            buyItem(Item.itemList[buy])
        elif buy == 'e' or buy == 'exit':
            break
        else: continue

def buyItem(item):
    global money, bonus
    if money >= item.price:
        dialogue(f'You purchased{item.article} {item.name}')
        money -= item.price
        bonus += item.buff/100
        if 'goldenPan' in item.tags: print('Your cooking skill has been maxed out!'); sklCooking.lvlup(999,True)
    else: dialogue('You have insufficent funds.')
    
def work():
    global money, bonus
    if has_job == True:
        dialogue("You spent the day at work.")
        bonus = round(bonus, 2)
        pay = wage * (bonus+1)
        dialogue(f'you earned {pay} money')
        money += pay
        progressDay()
    else: dialogue("You don't have a job.")

def cook():
    lowCookingDialouge = ["* lowCookingDialouge1", "* lowCookingDialouge2", "* lowCookingDialouge3"]
    medCookingDialouge = ["* medCookingDialouge1", "* medCookingDialouge2", "* medCookingDialouge3"]
    highCookingDialouge = ["* highCookingDialouge1", "* highCookingDialouge2", "* highCookingDialouge3"]
    if sklCooking.level < 5: dialogue(random.choice(lowCookingDialouge))
    elif sklCooking.level < 8 and sklCooking.level > 4 : dialogue(random.choice(medCookingDialouge))
    else: dialogue(random.choice(highCookingDialouge))
    if random.randint(0,10) <= 3: sklCooking.lvlup(1, True)

def main():
    global money
    lastaction = None
    dialogue("Day: " + str(day))
    checkWallet()
    #Main loop
    while True:
        action = (input("> ")).lower()
        if action.startswith("dev_") and not dev_mode: print("Invalid Action"); continue
        if action == 'r': action = lastaction
        else: lastaction = action
        if action == "wallet":
            checkWallet()
        elif action == "shop":
            openShop()
        elif action ==  "work":
            work()
        elif action == 'cook':
            cook()
        elif action == "sleep":
            progressDay()
                
        elif action == 'clear':
            clear()
        
        elif action == "quit":
            break
                
        elif action == "dev_bonus":
                print("Bonus: " + str(bonus))
        elif action == "dev_skilltest":
                sklCooking.lvlup(1, True)
                print(f'Cooking Skill: {sklCooking.level}')
        elif action == 'i need that golden pan':
            money += 99999999999
                
        else:
            print("Invalid Action")
                
if __name__ == "__main__": main()
else: print("Imported " + __name__)