from errors import InvalidSideError


def validate_side(obj) -> callable:
    def wrapper(side: str):
        if not (side.isdigit() and int(side) >= 1):
            raise InvalidSideError(f'\nYour value {side} is invalid, a side should a natural positive number')
        return obj(side)
    return wrapper
