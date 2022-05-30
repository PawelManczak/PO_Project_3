from dataclasses import dataclass


@dataclass(init=True, eq=True)
class Position:
    x: int
    y: int
