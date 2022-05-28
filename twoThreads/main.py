# This Python file uses the following encoding: utf-8
import os, sys
from pathlib import Path
from time import sleep

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, Signal, Slot, QThread


class FirstWorker(QObject):
    finished = Signal()
    counter = Signal(str)

    def __init__(self, parent=None):
        super(FirstWorker, self).__init__(parent)
        self.__finished = False

    @Slot()
    def doWork(self):
        print("First worker started")
        for i in range(101):
            if self.__finished:
                break
            self.counter.emit(str(i))
            sleep(0.1)
        self.finished.emit()


    def stop(self):
        print(f"[-] First worker stopped")
        self.__finished = True

class SecondWorker(QObject):
    finished = Signal()
    counter = Signal(str)

    def __init__(self, parent=None):
        super(SecondWorker, self).__init__(parent)
        self.__finished = False

    @Slot()
    def doWork(self):
        print("First worker started")
        for i in range(101):
            if self.__finished:
                break
            self.counter.emit(str(i))
            sleep(0.1)
        self.finished.emit()

    def stop(self):
        print(f"[-] Second worker stopped")
        self.__finished = True


class Handler(QObject):
    
    firstWorker = Signal(str)
    secondWorker = Signal(str)

    # FIRST WORKER THREAD
    def first_worker_signal(self, text):
        self.firstWorker.emit(text)

    @Slot()
    def first_worker_start(self):
        self.first_thread = QThread()
        self.first_worker = FirstWorker()
        self.first_worker.moveToThread(self.first_thread)

        self.first_thread.started.connect(self.first_worker.doWork)

        self.first_worker.counter.connect(self.first_worker_signal)
        self.first_worker.finished.connect(self.first_thread.quit)

        self.first_thread.start()

    @Slot()
    def first_worker_stop(self):
        print(f"[+] Пытаемся остановить первый поток")
        self.first_worker.stop()
        self.first_thread.quit()


    # SECOND WORKER THREAD
    def second_worker_signal(self, text):
        self.secondWorker.emit(text)

    @Slot()
    def second_worker_start(self):
        self.second_thread = QThread()
        self.second_worker = SecondWorker()
        self.second_worker.moveToThread(self.second_thread)

        self.second_thread.started.connect(self.second_worker.doWork)

        self.second_worker.counter.connect(self.second_worker_signal)
        self.second_worker.finished.connect(self.second_thread.quit)

        self.second_thread.start()

    @Slot()
    def second_worker_stop(self):
        print(f"[+] Пытаемся остановить второй поток")
        self.second_worker.stop()
        self.second_thread.quit()


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    handler = Handler()
    engine.rootContext().setContextProperty("handler", handler)

    engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
