from collections import defaultdict
from typing import Dict

from tinybones.index import Index
from tinybones.name import Name
from tinybones.slot import Slot


class Rows:
    def __init__(self) -> None:
        ...

    def __getitem__(self, key: int) -> dict:
        ...

    def add(self, slot: Slot) -> None:
        ...