from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class CropWindow(QMainWindow):
    """Main Window"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop Simulator")

def main():
    crop_simulation = QApplication(sys.argv)
    crop_window = CropWindow()
    crop_window.show()
    crop_window.raise_()
    crop_simulation.exec()

if __name__ == "__main__":
    main()
