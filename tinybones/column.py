from typing import Any, Iterator, List, Sequence

from tinybones.value import Value


class Column:
    def __init__(self) -> None:
        self.values: List[Value] = []

    def append(self, value: Value) -> None:
        self.values.append(value)

    def add(self, value: Value) -> None:
        self.append(value)

    def edit(self, key: int, value: Any) -> None:
        self.values[key].value = value

    def __getitem__(self, key: int) -> Any:
        return self.values[key].value

    def __setitem__(self, key: int, value: Any) -> None:
        self.edit(key, value)

    def __delitem__(self, key: int) -> None:
        self[key] = None

    def __len__(self) -> int:
        return len(self.values)

    def __iter__(self) -> Iterator:
        return iter(self.values)

    def __repr__(self) -> str:
        return f'Column({repr(self.values)})'

    def __str__(self) -> str:
        return str(self.values)
    
    def insert(self, index: int, object, /) -> None:
        """insert value at index"""
        self.values.insert(index, object)

    def reverse(self) -> None:
        """Reverse in place."""
        for i, val in enumerate(reversed(self.values)):
            self[i] = val

    def extend(self, values) -> None:
        for val in values:
            self.add(val)

    def pop(self) -> Any:
        value = self.values.pop().value

    def remove(self, value, /) -> None:
        """Remove first occurrence of value."""
        for i, item in enumerate(self.values):
            if item == value or item is value:
                self[i] = None

    def __iadd__(self, value) -> None:
        self.add(value)
