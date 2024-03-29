from typing import Self, overload

class Position:
    def __init__(self, idx: int, ln: int, col: int, fn: str, ftxt: str) -> None: ...
    @overload
    def advance(self) -> Self: ...
    @overload
    def advance(self, current_char: str) -> Self: ...
    def copy(self) -> Self: ...
