from Animal import Animal


class Mammal(Animal):
    has_teeth = True
    has_fur = True
    has_mammary_gland = True
    has_diaphragm = True
    milk = 0

    def give_a_birth(self, sex, weight):
        self.milk += 10
        return super().give_a_birth(sex, weight)

    def wet_nurse(self, child):
        if self.milk:
            dose_count = 1
            self.milk -= dose_count
            dose = {
                'protein': 4.8 * dose_count,  # примерная пищевая ценность молока
                'carbohydrate': 7.8 * dose_count,
                'fat': 4.1 * dose_count
            }
            child.feed(dose)
