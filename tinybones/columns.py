from collections import defaultdict
from typing import Dict, List, Sequence

from tinybones.name import Name
from tinybones.value import Value
from tinybones.slot import Slot


class Columns:
    def __init__(self, data):
        self.data = data

    def add(self, slot: Slot) -> None:
        ...

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return f'Columns({self})'

    def __getitem__(self, key: str) -> List[Slot]:
        ...