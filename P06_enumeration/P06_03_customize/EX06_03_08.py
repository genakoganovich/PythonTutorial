from enum import Enum
from functools import total_ordering


@total_ordering
class OrderedEnum(Enum):
    def __lt__(self, other):
        if isinstance(other, OrderedEnum):
            return self.value < other.value
        return NotImplemented


class ApprovalStatus(OrderedEnum):
    PENDING = 1
    IN_PROGRESS = 2
    APPROVED = 3

if __name__ == '__main__':
    status = ApprovalStatus(2)
    if status < ApprovalStatus.APPROVED:
        print('The request has not been approved.')
