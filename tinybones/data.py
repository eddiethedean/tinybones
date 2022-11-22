from collections import defaultdict
from typing import Union

from tinybones.column import Column
from tinybones.row import Row
from tinybones.value import Value


class Data:
    def __init__(self, data) -> None:
        self.columns = defaultdict(Column)
        self.rows = defaultdict(Row)
        self._store_data(data)

    def _store_data(self, data) -> None:
        for col, values in data.items():
            for i, value in enumerate(values):
                v = Value(value)
                self.columns[col].add(v)
                self.rows[i].add(col, v)

    def __str__(self) -> str:
        return str(dict(self.columns))
    
    def __repr__(self) -> str:
        return f'Data({self})'
    
    def __len__(self) -> int:
        return len(self.rows)

    def __setitem__(self, key, value) -> None:
        if isinstance(key, str):
            for i, val in enumerate(value):
                self.columns[key][i].value = val
        elif isinstance(key, int):
            for col, val in value.items():
                self.rows[key][col].value = val
        raise ValueError('key must be str or int')

    def __getitem__(self, key) -> Union[Column, Row]:
        if isinstance(key, str):
            return self.columns[key]
        elif isinstance(key, int):
            return self.rows[key]
        raise ValueError('key must be str or int')
    
