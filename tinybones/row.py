from typing import Any, Dict, ItemsView, KeysView, Mapping, Tuple, ValuesView

from tinybones.value import Value


class Row:
    def __init__(self) -> None:
        self.data: Dict[str, Value] = {}

    def __setitem__(self, key: str, value: Any) -> None:
        if key in self.data:
            self.replace(key, value)
        else:
            self.add(key, value)

    def __getitem__(self, key: str) -> Any:
        return self.data[key].value
    
    def __delitem__(self, key: str) -> None:
        """Set item value to None"""
        self.data[key].value = None

    def __iter__(self) -> KeysView:
        return self.data.keys()
    
    def __len__(self) -> int:
        return len(self.data)
    
    def __str__(self) -> str:
        return str(self.data)
    
    def __repr__(self) -> str:
        return f'Row({self.data})'
    
    def __contains__(self, value) -> bool:
        return value in self.data
    
    def __eq__(self, other: Mapping) -> bool:
        return self.data == other
    
    def __ne__(self, other: Mapping) -> bool:
        return self.data != other
    
    def add(self, key: str, value: Value) -> None:
        self.data[key] = value

    def replace(self, key: str, value: Any) -> None:
        self.data[key].value = value

    def keys(self) -> KeysView:
        return self.data.keys()

    def items(self) -> ItemsView:
        return self.data.items()

    def values(self) -> ValuesView:
        return self.data.values()
    
    def pop(self, key: str, default=None, /) -> Any:
        if key not in self and default is not None:
            return default
        value = self[key]
        del self[key]
        return value
    
    def popitem(self, key: str, default=None, /) -> Tuple[str, Any]:
        return key, self.pop(key, default)
    
    def clear(self) -> None:
        for col in self.keys():
            self[col].value = None

    def update(self, other) -> None:
        self.data.update(other)

    def setdefault(self, key: str, default=None, /):
        """
        Insert key with a value of default if key is not in the dictionary.

        Return the value for key if key is in the dictionary, else default.
        """
        if key not in self:
            self[key] = default
        return self[key]
    
    def get(self, key: str, default=None, /) -> Any:
        """Return the value for key if key is in the row, else default.)"""
        if key not in self.keys():
            return default
        return self[key]

    