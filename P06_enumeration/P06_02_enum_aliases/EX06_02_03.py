from enum import Enum


class ResponseStatus(Enum):
    # in progress
    IN_PROGRESS = 1
    REQUESTING = 1
    PENDING = 1

    # success
    SUCCESS = 2
    OK = 2
    FULFILLED = 2

    # error
    ERROR = 3
    NOT_OK = 3
    REJECTED = 3

if __name__ == '__main__':
    code = 'OK'
    if ResponseStatus[code] is ResponseStatus.SUCCESS:
        print('The request completed successfully')

    code = 'FULFILLED'
    if ResponseStatus[code] is ResponseStatus.SUCCESS:
        print('The request completed successfully')
