import sys
from PyQt5 import QtWidgets

def window():
    application = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    widget.setGeometry(100,100,200,200)
    widget.show()
    sys.exit(application.exec_())

window()
