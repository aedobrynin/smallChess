import sys
import os
from PyQt5.QtGui import QColor
from chess import WHITE, BLACK

FIELD_SIZE = 360

CELL_SIZE = FIELD_SIZE // 8

BLACK_CELL_COLOR = QColor(118, 150, 85)
WHITE_CELL_COLOR = QColor(241, 236, 214)

P_DIR = "./Pieces/"  # Piece images directory
P_EXT = ".png"  # Piece images extension

DB_PATH = "./statistics.db"


def resourcePath(relativePath):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    basePath = getattr(sys,
                       '_MEIPASS',
                       os.path.dirname(os.path.abspath(__file__)))

    return os.path.join(basePath, relativePath)
