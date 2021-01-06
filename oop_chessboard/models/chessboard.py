from oop_chessboard.models.side import Side


class Chessboard:
    def __init__(self, height: Side, width: Side):
        self.width = width
        self.height = height

    def __repr__(self):
        result = ''
        for row in range(int(self.height)):
            for cell in range(int(self.width)):
                result += '*' if row % 2 == cell % 2 else ' '
            result += '\n'
        return result
