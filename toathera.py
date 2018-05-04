import sys


from PyQt4 import QtCore, QtGui
from ui import Ui_MainWindow

class StartUI(QtGui.QMainWindow):
    '''Build an instance of the GUI'''
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    gui = StartUI()
    gui.show()
    sys.exit(app.exec_())