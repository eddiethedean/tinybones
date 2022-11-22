from typing import Union


class Key:
    def __init__(self, value: Union[str, int]) -> None:
        self.value = value