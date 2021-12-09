from __future__ import annotations
from itertools import islice
from dataclasses import dataclass
from typing import Iterable, Callable, List


@dataclass
class Seq:
    sequence: Iterable[int]

    def filter(self, func: Callable) -> Seq:
        return Seq(filter(func, self.sequence))

    def map(self, func: Callable) -> Seq:
        return Seq(map(func, self.sequence))

    def take(self, n: int) -> List[int]:
        return list(islice(self.sequence, 0, n))


if __name__ == '__main__':
    numbers = (1, 2, 3, 4, 5)
    seq = Seq(numbers)
    res = seq.filter(lambda n: n % 2 == 0).map(lambda n: n + 10).take(3)
    assert res == [12, 14]