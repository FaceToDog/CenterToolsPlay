import sys
import time
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit
from PyQt5.Qt import QThread
from 界面.lotteryTicket import Ui_twoColorPlay


class EmitStr(QObject):
    '''
    定义一个信号类，
    sys.stdout有个write方法，通过重定向，
    每当有新字符串输出时就会触发下面定义的write函数，
    进而发出信号
    text：新字符串，会通过信号传递出去
    '''
    textWrit = pyqtSignal(str)

    def write(self, text):
        self.textWrit.emit(str(text))


class MyWidget(QWidget):  # 定义一个窗体类，继承于QWidget
    def __init__(self):
        super().__init__()
        self.ui = Ui_twoColorPlay()
        self.ui.setupUi(self)
        sys.stdout = EmitStr(textWrit=self.outputWrite)  # 输出结果重定向
        sys.stderr = EmitStr(textWrit=self.outputWrite)  # 错误输出重定向
        self.ui.pushButton.clicked.connect(self.printText)

    def outputWrite(self, text):
        self.ui.textEdit.append(text)  # 输出的字符追加到 QTextEdit 中

    def printText(self):
        print("hello")


class MyThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            time.sleep(0.5)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    w = MyWidget()
    mythread = MyThread()
    mythread.start()
    mythread.finished.connect(lambda: print('完成打印'))
    w.show()
    sys.exit(app.exec())
