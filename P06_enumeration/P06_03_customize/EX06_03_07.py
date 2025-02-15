from enum import Enum
from functools import total_ordering


@total_ordering
class OrderedEnum(Enum):
    def __lt__(self, other):
        if isinstance(other, OrderedEnum):
            return self.value < other.value
        return NotImplemented
