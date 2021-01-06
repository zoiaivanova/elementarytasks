from oop_chessboard.decorators.validate_side import validate_side


@validate_side
class Side:
    def __init__(self, side):
        self._value = side

    def __int__(self):
        return int(self._value)
