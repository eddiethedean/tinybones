from collections import defaultdict
from tabulate import tabulate

from typing import Mapping, Sequence, Union
from tinybones.column import Column
from tinybones.row import Row

from tinybones.value import Value


class Grid:
    def __init__(
        self,
        data: Mapping[str, Sequence]
    ) -> None:
        self.columns = defaultdict(Column)
        self.rows = defaultdict(Row)
        for col, values in data.items():
            for i, value in enumerate(values):
                v = Value(value)
                self.columns[col].append(v)
                self.rows[i][col] = v

    def __repr__(self) -> str:
        return tabulate(self.columns, tablefmt='grid', headers=list(self.columns.keys()))

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

    