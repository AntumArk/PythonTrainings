from enum import IntEnum, Enum


class TicTacValues(IntEnum):
    """Enumerator for game logic"""

    Z = 0
    X = 1
    O = -1


class TicTacGameResults(IntEnum):
    IN_PROGRESS = 0
    X_WON = 1
    O_WON = 2
    TIE = 3


class TicTacChars(Enum):
    """Enumerator for characters used in drawing TicTacToe"""

    Z = " "
    X = "❌"
    O = "⭕"
    H_LINE = "─"
    V_LINE = "│"
    H_CROSS = "┼"
