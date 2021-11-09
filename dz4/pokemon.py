from random import choice
import abc


class AnimeMon:

    @property
    @abc.abstractmethod
    def exp(cls):
        pass

    @abc.abstractmethod
    def inc_exp(self, val):
        pass


class Pokemon(AnimeMon):

    def __init__(self, name, poketype: str = ''):
        self.name = name
        self.poketype = poketype
        self._exp = 0

    @property
    def exp(self):
        return self._exp

    def inc_exp(self, value: int):
        self._exp += value

    def __str__(self):
        return f'{self.name}/{self.poketype}'


class Digimon(AnimeMon):

    def __init__(self, name):
        self.name = name
        self._exp = 0

    @property
    def exp(self):
        return self._exp

    def inc_exp(self, value: int):
        self._exp += value * 8

    def __str__(self):
        return f'{self.name}'


def train(pokemon: Pokemon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - pokemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = choice([True, False])
        if win:
            pokemon.inc_exp(step_size)


if __name__ == '__main__':
     bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
     agumon = Digimon(name='Agumon')

     for pokemon in (bulbasaur, agumon):
         train(pokemon)
         print(f'- {pokemon}, опыт = {pokemon.exp}')