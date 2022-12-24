class Annie:
    def __init__(self, health, mana, AP):
        self.health = health
        self.mana = mana
        self.AP = AP

    def tibbers(self):
        damage = self.AP * 0.65 + 400

        print('티버: 피해량 ', damage)


a = Annie(1803.68, 1184.0, 645)

a.tibbers()
