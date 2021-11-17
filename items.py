class Item:
    def __init__(this, name, price=0, buff=0):
        this.name = name
        this.price = price
        this.buff = buff
    
itmCoffee = Item("Coffee", 3, 5)
itmTest = Item("Test", 1, 15)