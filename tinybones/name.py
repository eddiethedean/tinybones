

class Name:
    def __init__(self, name: str) -> None:
        self.first_value: str = name
        self.value: str = name

    def __hash__(self) -> int:
        return hash(self.first_value)

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f'Name({self})'

    def __eq__(self, other) -> bool:
        return self.value == other