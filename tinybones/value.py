from typing import Any


class Value:
    def __init__(self, value: Any) -> None:
        self.value: Any = value

    def __hash__(self) -> int:
        return hash(self.value)

    def __str__(self) -> str:
        return str(self.value)
    
    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other) -> bool:
        return self.value == other