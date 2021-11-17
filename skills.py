class Skill:
    skillList = []
    def __init__(this, name):
        this.name = name
        this.level = 0
        Skill.skillList.append(this.name)
        
    def lvlup(this, amount, message=None):
        this.level += amount
        if message == True:
            print(f'\"{this.name}\" skill increased!')
        
sklCooking = Skill("Cooking")
sklDance = Skill("Dance")