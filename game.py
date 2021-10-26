day = 0
gold = 10
goldPerDay = 20

def progressDay():
  global day
  global gold
  day += 1
  gold += goldPerDay 
def openShop():
  exec(open("shop.py").read())
def checkGold():
  print("Gold: " + str(gold))



checkGold()
while True:
  action = (input(">"))
  
  if action == "d":
    print(day)
  elif action == "g":
    checkGold()
  elif action == "shop":
    openShop()
  elif action == "sleep":
    progressDay()
  else:
    print("Invalid Action")
