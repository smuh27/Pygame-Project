
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def set_score(self, score):
        self.score = score
    
    def increase_score(self, points):
        self.score += points 

text = Player('Samir')

print(text.name)