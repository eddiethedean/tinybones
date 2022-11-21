from collections import defaultdict
from typing import Mapping, Sequence, Union


DataMapping = Mapping[str, Sequence]


class Table:
    def __init__(self, data: DataMapping) -> None:
        self.rows = defaultdict(dict)
        self.columns = defaultdict(list)
        for col, values in data.items():
            for i, value in enumerate(values):
                self.rows[i][col] = value
                self.columns[col].append(value)

    def __getitem__(self, key: Union[str, int]) -> Union[list, dict]:
        if isinstance(key, int):
            return self.rows[key]
        elif isinstance(key, str):
            return self.columns[key]
        raise ValueError('key must be string or int')

    def __str__(self) -> str:
        return str(dict(self.columns))

    def __repr__(self) -> str:
        return f'Table({self})'

    def __setitem__(self, key, value) -> None:
        if isinstance(key, int):
            if isinstance(value, dict):
                for col in value:
                    self.rows[key][col] = value
            elif isinstance(value, list):
                for col, v in zip(self.rows, value):
                    self.rows[col] = v
            else:
                for col in self.rows:
                    self.rows[col] = value
        elif isinstance(key, str):
            if isinstance(value, list):
                self.columns[key] = value
            else:
                self.columns[key] = [v for v in value]
        raise ValueError('key must be string or int')
