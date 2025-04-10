# Basic interface template
class Combo:
    def getCost(self):
        pass

    def getDepth(self):
        return 0
    
    def get_max_depth(self): 
        return 0

# Combo 1 and Combo 2 both start with 0 wrappers but 
# have different wrappers max depths
class Combo1(Combo):
    def getCost(self):
        return 6.99

    def getDepth(self):
        return 0
    
    def getMaxDepth(self): 
        return 1

class Combo2(Combo):
    def getCost(self):
        return 6.99
    
    def getDepth(self):
        return 0

    def getMaxDepth(self): 
        return 2
    
# Wrapper interface
class ComboMeal(Combo):
    def __init__(self, combo):
        self._combo = combo
        current_depth = self.getDepth()
        max_depth = self.getMaxDepth()

        if current_depth > max_depth:
            raise Exception(f"Exceeded max decorator depth of {max_depth} for this coffee.")
    
    def getCost(self):
        return self._combo.getCost()
    
    def getDepth(self):
        return self._combo.getDepth() + 1

    def getMaxDepth(self): 
        return self._combo.getMaxDepth()
    
# Different meals as wrappers
# Different types of meals have different costs
class OrangeChicken(ComboMeal):
    def getCost(self):
        return self._combo.getCost() + 2.5
    
class SoyBroccoli(ComboMeal):
    def getCost(self):
        return self._combo.getCost() + 2
    
# Implementations
combo1 = Combo1()
combo2 = Combo2()

# Wrappers
combo1 = OrangeChicken(combo1)

combo2 = OrangeChicken(combo2)
combo2 = SoyBroccoli(combo2)

# Print total cost
print(f"Total cost of Combo 1: ${combo1.getCost():.2f}")
print(f"Total cost of Combo 2: ${combo2.getCost():.2f}")

