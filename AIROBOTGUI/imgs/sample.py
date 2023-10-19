
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
from PyQt5.QtGui import QMovie
state = 0
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # Resize main window to be 600px / 400px
        self.resize(800, 800)
        self.MovieLabel = QLabel(self)
        # Set gif content to be same size as window (600px / 400px)
        self.MovieLabel.setGeometry(QtCore.QRect(0, 0, 600, 400))
        self.movie = QMovie("BOT.gif")
        self.MovieLabel.setMovie(self.movie)
        self.movie.start()
        
        self.btn = QPushButton("Click", self)
        self.btn.setGeometry(QtCore.QRect(500, 50, 100, 50))
        self.btn.clicked.connect(lambda: self.stop_ani())
        
    def stop_ani(self):
        global state
        if state == 0:
            state = 1
            self.movie.stop()
            self.movie.jumpToFrame(1)
        else:
            state = 0
            self.movie.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())