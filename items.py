class Item:
    itemList = {}
    def __init__(self, name, price=0, buff=0, article='',tags=[]):
        self.name = name
        self.price = price
        self.buff = buff
        self.tags = tags
        if article != '': self.article = f' {article}'
        else: self.article = article
        Item.itemList[self.name.lower()] = self
    
itmCoffee = Item("Coffee", 3, 5, 'a')
itmEnergyDrink = Item("Energy Drink", 5, 10, 'an')
itmMilk = Item('Milk', 6, 12,)
itemGoldenPan = Item("Golden Pan", 99999999999, 0,'The',['goldenPan'])