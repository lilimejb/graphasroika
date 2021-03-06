import sys

from main import GraphMaker

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('grafi.ui', self)
        self.text.setFontPointSize(30)
        self.make_graph_button.clicked.connect(self.set_graph)

    def set_graph(self):
        matrix = [elem.split() for elem in self.text.toPlainText().split('\n')][:-1]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])
        maker = GraphMaker(matrix)
        maker.make_image()
        pixmap = QPixmap('plot.png')
        self.image.setPixmap(pixmap)
        self.image.setScaledContents(True)
    
    def count_roads(self, matrix):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
