class Animal:
    it_alive = True
    has_brain = True
    has_heart = True
    has_nerves = True
    weight = 0  # kilograms
    sex = None  # 'm' or 'f'
    it_pregnant = None

    def __init__(self, sex, weight):
        self.sex = sex
        self.weight = weight

    def feed(self, food):
        self.eat(food)

    def eat(self, food):
        calories = ((food['protein'] * 4) + (food['carbohydrate'] * 4) + (food['fat'] * 9))
        self.digestion(calories)

    def digestion(self, calories):
        self.gain(calories)

    def gain(self, calories):
        self.weight += (calories / 1000)  # (calories / 1000) for example

    def reproduce(self, partner):
        if self.it_alive and self.sex != partner.sex:
            if self.sex == 'f':
                self.it_pregnant = True
            else:
                partner.it_pregnant = True

    def give_a_birth(self, sex, weight):
        if self.it_pregnant:
            return self.__class__(sex, weight)
