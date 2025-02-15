from enum import Enum, auto


class State(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    PENDING = auto()
    FULFILLED = auto()
    REJECTED = auto()

if __name__ == '__main__':
    for state in State:
        print(state.name, state.value)