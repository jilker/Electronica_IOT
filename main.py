from typing import Tuple
from ventana import *
import threading
def call_window():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
if __name__ == "__main__":
    window_t=threading.Thread(target=call_window)
    window_t.start()
    