from enum import Enum


class PaymentStatus(Enum):
    PENDING = 1
    COMPLETED = 2
    REFUNDED = 3

    def __str__(self):
        return f'{self.name.lower()}({self.value})'

if __name__ == '__main__':
    print(PaymentStatus.PENDING)
    