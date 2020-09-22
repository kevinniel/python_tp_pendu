class Player:

    def __init__(self):
        self.name = ""
        self.ask_name()
        self.points = 0

    def ask_name(self):
        self.name = input('quel est votre prénom ?')

    def add_points(self, number):
        self.points += number
