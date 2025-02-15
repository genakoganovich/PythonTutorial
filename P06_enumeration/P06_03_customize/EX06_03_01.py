from enum import Enum


class PaymentStatus(Enum):
    PENDING = 1
    COMPLETED = 2
    REFUNDED = 3

if __name__ == '__main__':
    print(PaymentStatus.PENDING)
    