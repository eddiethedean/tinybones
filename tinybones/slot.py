from dataclasses import dataclass
from typing import Any

from tinybones.index import Index
from tinybones.name import Name
from tinybones.value import Value


@dataclass
class Slot():
    index: Index
    column_name: Name
    value: Value
