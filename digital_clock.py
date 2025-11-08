import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QIcon


class DigitalCLock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setFixedSize(300, 100)
        self.setWindowIcon(QIcon("Images and icons/clock.png"))

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setStyleSheet("font-family: Calbiri;"
                                      "font-size: 36px;"
                                      "color: #333;")

        self.time_label.setAlignment(Qt.AlignCenter)

        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)

    def show_time(self):
        current_time = QTime.currentTime().toString('hh:mm:ss')
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalCLock()
    clock.show()
    sys.exit(app.exec_())