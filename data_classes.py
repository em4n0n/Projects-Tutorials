from dataclasses import dataclass, field

@dataclass
class Investor:
    name: str
    age: int
    cash: float = field(repr=False)

    def __repr__(self):
        return "Hello"

i1 = Investor("John", 80, 700)
i2 = Investor("Mike", 18, 2000)
i3 = Investor("John", 80, 900)

print(i1)