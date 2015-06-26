import random
class Card():
    def __init__(self):
        self.genetor()

    def genetor(self):
        weighted_choices = [('Yellow', 1), ('Green', 4)]
        population = [val for val, cnt in weighted_choices for i in range(cnt)]
        self.color = random.choice(population)
        self.number = str(random.randrange(1))
        print (self.color, self.number)
        return (self.color, self.number)

