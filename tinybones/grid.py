from collections import defaultdict
from typing import Any, Dict, ItemsView, Iterator, KeysView, Mapping, Sequence, Union, ValuesView
from tinybones.column import Column

from tinybones.row import Row
from tinybones.value import Value


class Grid:
    def __init__(self, data) -> None:
        self._columns = defaultdict(Column)
        self._rows = defaultdict(Row)
        self._store_data(data)

    def _store_data(self, data) -> None:
        # if data is Mapping[str, Sequence]
        self._store_columns(data)

    def _store_columns(self, columns: Mapping[str, Sequence]) -> None:
        for col, values in columns.items():
            self.add_column(col, values)

    def _store_rows(self, rows: Sequence[Mapping[str, Any]]) -> None:
        for row in rows:
            self.add_row(row)

    def __str__(self) -> str:
        return str(dict(self._columns))
    
    def __repr__(self) -> str:
        return f'Grid({self})'
    
    def __len__(self) -> int:
        return len(self._rows)

    def __setitem__(self, key, value) -> None:
        if isinstance(key, str):
            if key in self._columns:
                for i, val in enumerate(value):
                    self._columns[key][i].value = val
            else:
                self.add_column(key, value)
        elif isinstance(key, int):
            if key in self._rows:
                for col, val in value.items():
                    self._rows[key][col].value = val
            else:
                self.add_row(value)
        else:
            raise ValueError('key must be str or int')

    def __getitem__(self, key) -> Union[Column, Row]:
        if isinstance(key, str):
            return self._columns[key]
        elif isinstance(key, int):
            return self._rows[key]
        raise ValueError('key must be str or int')
    
    def __iter__(self) -> Iterator:
        return iter(self._rows)
    
    def __contains__(self, value) -> bool:
        return value in self.columns.values() or value in self.rows.values()
    
    def add_column(self, name: str, values: Sequence) -> None:
        for i, val in enumerate(values):
            v = Value(val)
            self._columns[name].add(v)
            self._rows[i].add(name, v)
            # TODO: add None for missing rows

    def add_row(self, row: Mapping[str, Any]) -> None:
        for col, value in row.items():
            v = Value(value)
            self._columns[col].add(v)
            self._rows[len(self)].add(col, v)
            # TODO: add None for missing columns

    @property
    def rows(self) -> Dict[int, Row]:
        return dict(self._rows)
    
    @property
    def columns(self) -> Dict[str, Column]:
        return dict(self._columns)
    
    def keys(self) -> KeysView:
        both = {**self._columns, **self._rows}
        return both.keys()
    
    def items(self) -> ItemsView:
        both = {**self._columns, **self._rows}
        return both.items()
    
    def values(self) -> ValuesView:
        both = {**self._columns, **self._rows}
        return both.values()
    
    def get(self, key, default=None, /) -> Any:
        if key not in self.keys():
            return default
        return self[key]
    
    def __eq__(self, other: Mapping) -> bool:
        return {**self._columns, **self._rows} == other

    def __ne__(self, other: Mapping) -> bool:
        return {**self._columns, **self._rows} != other
    
    

    