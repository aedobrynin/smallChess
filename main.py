import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from Cell import Cell
import Ui

FIELD_SIZE = (360, 360)
BLACK_CELL_COLOR = QtGui.QColor(118, 150, 85)
WHITE_CELL_COLOR = QtGui.QColor(241, 236, 214)

class MainWindow(QtWidgets.QMainWindow, Ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.setGeometry(710, 390, 600, 600)

        for row in range(8):
            for col in range(8):
                cell = Cell(self, row, col,
                            FIELD_SIZE[0] // 8, FIELD_SIZE[1] // 8)

                if (row + col) % 2 == 1:
                    cell.setColor(BLACK_CELL_COLOR)
                else:
                    cell.setColor(WHITE_CELL_COLOR)

                cell.setFigure("./p.png")

                self.chessCellsGridLayout.addWidget(cell, row, col)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
