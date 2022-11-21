from typing import Any, Dict, ItemsView, KeysView, ValuesView

from tinybones.value import Value


class Row:
    def __init__(self) -> None:
        self.data: Dict[str, Value] = {}

    def __setitem__(self, key: str, value: Any) -> None:
        if key in self.data:
            self.data[key].value = value
        else:
            self.data[key] = value

    def __getitem__(self, key: str) -> Any:
        return self.data[key].value

    def keys(self) -> KeysView:
        return self.data.keys()

    def items(self) -> ItemsView:
        return self.data.items()

    def values(self) -> ValuesView:
        return self.data.values()

    def __repr__(self) -> str:
        return repr(self.data)

    def __str__(self) -> str:
        return str(self.data)