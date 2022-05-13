from dialogue import dialogue, dialogue_ellipsis, dialogue_input, clear

class Skill:
    skillList = []
    def __init__(self, name):
        self.name = name
        self.level = 0
        Skill.skillList.append(self.name)
        
    def lvlup(self, amount, message=None):
        self.level += amount
        if message == True:
            dialogue(f'\"{self.name}\" skill increased to level {self.level}!')
        
sklCooking = Skill("Cooking")