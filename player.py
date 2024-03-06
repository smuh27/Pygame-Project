class Player:
    def __init__(self, name):
        self.score = 0
        self.name = name


    def set_score(self, score):
        self.score = score
    
    def increase_score(self, points):
        self.score += points 
