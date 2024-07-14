element_isStrongAgainst = {"fire": "grass", "water": "fire", "grass": "water", "electric": "water", "ground": "electric"}
element_isWeakAgainst = {"fire": "water", "water": "grass", "grass": "fire", "electric": "ground", "ground": "water"}


type Pokemon = Pokemon

class NoPokemonException(Exception):
        def __init__(self, message):
            super().__init__(message)
class Pokemon:
    def __init__(self, name, level, typ):
        self.name = name
        self.level = level
        self.typ = typ
        self.hp = 3 * level
        self.isInPokeball = True

    def callBackOrRelease(self):
        if self.isInPokeball:
            self.isInPokeball = False
            return "Pokemon ist nun Befreit"
        else:
            self.isInPokeball = True
            return "Pokemon ist nun im Pokeball"

    def scanWithPokedex(self):
        return f"Name {self.name}\n Level {self.level}\n Type {self.typ} \n Healthstatus: {"Good" if self.hp > (self.level * 3 / 2) else "Bad"}"

    def attack(self, other: Pokemon):
        if other.isInPokeball:
            raise NoPokemonException("Anderes Pokemon ist in Pokeball")

        if type(other) is not Pokemon:
            raise NoPokemonException("Ziel ist kein Pokemon")

        is_weak = element_isStrongAgainst[other.typ] == self.typ
        is_strong = element_isWeakAgainst[other.typ] == self.typ
        print(is_weak)
        print(is_strong)

        if is_strong:
            other.hp -= self.level * 2
            print("Das war sehr effektiv!")
        elif is_weak:
            other.hp -= self.level / 2
            print("Das war nicht so effektiv!")
        else:
            other.hp -= self.level
            print("Weder effektiv noch ineffektiv")

        if(other.hp <= 0):
            other.hp = 0
            print(f"{other.name} wurde besiegt und ist Kampfünfähig")
        print(f"{other.name} hat noch {other.hp}HP Übrig")
        other.callBackOrRelease()



