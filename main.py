from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from main_form import Ui_MainWindow
import matplotlib.pyplot as plt
from pydicom import dcmread
import sys
from PyQt5.QtWidgets import QMessageBox

class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionupload_file.triggered.connect(self.btn_convert_clicked)

    def btn_convert_clicked(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open file', 'd:\\', "DICOM files (*.dcm)")
            fn = fname[0]
            ds = dcmread(fn)
            arr = ds.pixel_array
            plt.imshow(arr, cmap="gray")
            plt.show()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('An error occurred while loading the file')
            msg.setWindowTitle("Error")
            msg.exec_()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    sys.exit(app.exec())