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

    def __len__(self) -> int:
        return len(self.values)

    def __iter__(self) -> Iterator:
        return iter(self.values)

    def __repr__(self) -> str:
        return f'Column({repr(self.values)})'

    def __str__(self) -> str:
        return str(self.values)

