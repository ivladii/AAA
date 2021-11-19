from __future__ import annotations
from abc import abstractmethod


class ComputerColor:

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __mul__(self, value: float):
        pass

    @abstractmethod
    def __rmul__(self, value: float):
        pass


class Color(ComputerColor):

    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, other: Color) -> Color:
        return all((self.r == other.r,
                    self.g == other.g,
                    self.b == other.b))

    def __add__(self, other: Color) -> Color:
        return Color(self.r + other.r,
                     self.g + other.g,
                     self.b + other.b)

    @staticmethod
    def opacity(color_code: int, c: float) -> int:
        if not 0 <= c <= 1:
            raise ValueError('value between 0 and 1')

        cl = -256 * (1 - c)
        F = (259 * (cl + 255)) / (255 * (259 - cl))
        new_color_code = int(F * (color_code - 128) + 128)

        return new_color_code

    def __mul__(self, c: float) -> Color:
        return Color(Color.opacity(self.r, c),
                     Color.opacity(self.g, c),
                     Color.opacity(self.b, c))

    __rmul__ = __mul__

    def __hash__(self) -> int:
        return hash((self.r,
                     self.g,
                     self.b))

    def __str__(self) -> str:
        start = '\033[1;38;2'
        end = '\033[0'
        mod = 'm'
        string = f'{start};{self.r};{self.g};{self.b}{mod}●{end}{mod}'
        return string

    __repr__ = __str__


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
    [bg_color] * 19,
    [bg_color] * 9 + [color] + [bg_color] * 9,
    [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
    [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
    [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
    [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
    [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
    [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
    [bg_color] * 19,
    ]
    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))


if __name__ == '__main__':
    purple = Color(139, 0, 255)
    print_a(purple)