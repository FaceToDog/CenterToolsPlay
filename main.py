import sys
import time
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit
from PyQt5.Qt import QThread


class EmitStr(QObject):
    '''
    定义一个信号类，
    sys.stdout有个write方法，通过重定向，
    每当有新字符串输出时就会触发下面定义的write函数，
    进而发出信号
    text：新字符串，会通过信号传递出去
    '''
    textWrit  = pyqtSignal(str)
    def write(self, text):
        self.textWrit.emit(str(text))


class MyWidget(QWidget):    # 定义一个窗体类，继承于QWidget
    def __init__(self):
        super().__init__()
        self.step_up()      # 构建一个QTextEdit， 以及对窗体的一些基本设置
        sys.stdout = EmitStr(textWrit=self.outputWrite)     # 输出结果重定向
        sys.stderr = EmitStr(textWrit=self.outputWrite)     # 错误输出重定向

    def outputWrite(self, text):
        self.te.append(text)       # 输出的字符追加到 QTextEdit 中

    def step_up(self):
        self.setWindowTitle('输出重定向')
        self.resize(500,500)
        self.te = QTextEdit(self)
        self.te.move(10,10)


class MyThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(10):
            print(i)
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
