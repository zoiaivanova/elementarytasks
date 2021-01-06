from oop_chessboard.errors.invalid_side_error import InvalidSideError


def validate_side(obj) -> callable:
    def wrapper(side: str):
        if not (side.isdigit() and int(side) >= 1):
            raise InvalidSideError(f'Your value {side} is invalid, a side should a natural positive number')
        return obj(side)
    return wrapper
