

class Index:
    def __init__(self, i: int) -> None:
        self.value = i

    def __hash__(self) -> int:
        return hash(self.value)

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f'Index({self})'

    def __eq__(self, other) -> bool:
        return self.value == other