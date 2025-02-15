from enum import Enum, auto


class State(Enum):
    PENDING = auto()
    FULFILLED = auto()
    REJECTED = auto()

    def __str__(self):
        return f'{self.name(self.value)}'

if __name__ == '__main__':
    for state in State:
        print(state.name, state.value)
