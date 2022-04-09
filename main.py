# ************************** man hinh loai 2 *************************
import sys
# pip install pyqt5
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.my_qtimer = QTimer(self)
        # self.widget_counter_int = None
        self.seconds = 0
        self.hours = 0
        self.minutes = 0
        self.uic.textEdit.setAlignment(Qt.AlignHCenter)
        self.uic.textEdit.setText("10:20:30")

        self.uic.Button_start.clicked.connect(self.timer_start)
        self.uic.Button_stop.clicked.connect(self.time_stop)
        self.uic.Button_clear.clicked.connect(self.time_clear)

    def time_clear(self):
        self.uic.textEdit.setText("00:00:00")

    def time_stop(self):
        self.my_qtimer.disconnect()

    def timer_start(self):
        # take data from textedit
        data = self.uic.textEdit.toPlainText()
        print(data.split(":"))
        list = data.split(":")

        second = int(list[2])
        minute = int(list[1])
        hour = int(list[0])

        # calculate total seconds
        if second > 0 or minute > 0 or hour > 0:
            self.total_seconds = hour * 3600 + minute * 60 + second

            self.my_qtimer.timeout.connect(self.timer_calculate)
            self.my_qtimer.start(1000)

    def timer_calculate(self):
        self.total_seconds -= 1

        self.hours = self.total_seconds // 3600

        total_seconds_for_minutes_and_seconds = self.total_seconds - (self.hours * 3600)
        self.minutes = total_seconds_for_minutes_and_seconds // 60

        self.seconds = total_seconds_for_minutes_and_seconds - (self.minutes * 60)

        if self.total_seconds <= 0:
            self.my_qtimer.disconnect()

        self.update_timer()

    def update_timer(self):
        self.uic.textEdit.setText("{:02d}:{:02d}:{:02d}".format(int(self.hours),
                                                                int(self.minutes),
                                                                int(self.seconds)))
        self.uic.textEdit.setAlignment(Qt.AlignHCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
