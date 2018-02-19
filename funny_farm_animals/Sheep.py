from Mammal import Mammal
from get_random_sex import get_random_sex
from get_random_weight import get_random_weight


class Sheep(Mammal):
    herd_instinct = True


sheep = Sheep('f', get_random_weight(50))
ram = Sheep('m',  get_random_weight(80))

sheep.reproduce(ram)

lamb = sheep.give_a_birth(Sheep, get_random_sex(), get_random_weight(20))
