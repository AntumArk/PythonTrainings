from enum import IntEnum, Enum


class TicTacValues(IntEnum):
    """Enumerator for game logic"""

    Z = 0
    X = 1
    O = -1
    TIE = 2


class TicTacChars(Enum):
    """Enumerator for characters used in drawing TicTacToe"""

    Z = " "
    X = "❌"
    O = "⭕"
    H_LINE = "─"
    V_LINE = "│"
    H_CROSS = "┼"
