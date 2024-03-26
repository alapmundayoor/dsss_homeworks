import sys
from PyQt5.QtWidgets import (
    QApplication, QPushButton, QWidget, QMainWindow,
    QFileDialog, QGridLayout, QVBoxLayout, QMessageBox, QComboBox
)
from PyQt5.QtCore import Qt, pyqtSignal
import pyqtgraph as pg
import imageio.v2 as io
import json
from PyQt5 import QtWidgets


class DropDown(QComboBox):
    def __init__(self, items):
        super().__init__()
        self.items = items
        self.addItems(self.items)

class ImageViewer(pg.ImageView):
    fileDropped = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    

class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.l = QGridLayout(self)
        self.imv = ImageViewer()
        self.l.addWidget(self.imv)
        self.setAcceptDrops(True)
    def dragEnterEvent(self, event):
            if event.mimeData().hasImage:
                event.accept()
            else:
                event.ignore()
        
    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction()
        else:
            event.ignore()
            
    def dropEvent(self, event):
        if event.mimeData().hasImage:
            fn = event.mimeData().urls()[0].toLocalFile()
            self.im = io.imread(fn)
            self.imv.setImage(self.im)
            event.accept()
        else:
            event.ignore()

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.set_defaults()

        w = QWidget(self)
        self.setCentralWidget(w)
        self.mainLayout = QVBoxLayout()
        w.setLayout(self.mainLayout)

        self.setMinimumSize(250, 300)

        self.imageViewer = Interface()
        self.mainLayout.addWidget(self.imageViewer)

        self.openButton = QPushButton()
        self.openButton.setGeometry(300, 300, 350, 300)
        self.openButton.setText("Open Image")
        self.openButton.clicked.connect(self.open)

        self.mainLayout.addWidget(self.openButton)
        self.mainLayout.addStretch(1)

        # Set up the image saving shortcut
        save_shortcut = QtWidgets.QShortcut(("Ctrl+S"), self)
        save_shortcut.activated.connect(self.save_image)

        # Connect fileDropped signal to handle_file_dropped slot
        self.imageViewer.imv.fileDropped.connect(self.handle_file_dropped)

    def set_defaults(self): ## Set default values for the application
        # Settings for the window:
        self.status = self.statusBar()
        # Initialize the variable containing the image 
        self.im = None 

        ## Load the settings from the json file
        with open ("newsettings.json", "r") as jsonfile:
            self.options = json.load(jsonfile)
        width = self.options["defaults"]["width"]
        height = self.options["defaults"]["height"]
        self.resize(width, height)
        self.setWindowTitle(self.options["title"]["english"]["window title"])

        
    def save_image(self):
        if self.im is not None:
            fn, _ = QFileDialog.getSaveFileName(self, 'Save Image', filter="*.png *.jpg")
            if fn:
                io.imwrite(fn, self.im)
                self.show_message("Image was saved successfully!")
            else:
                self.show_message("Error trying to save the image!", is_error=True)

    def open(self):
        fn, _ = QFileDialog.getOpenFileName(filter="*.png *.jpg")
        if fn:
            self.status.showMessage(fn)
            self.im = io.imread(fn)
            self.imageViewer.imv.setImage(self.im)
            self.show_message("Image successfully loaded!")
        else:
            self.show_message("Something went wrong!", is_error=True)

    def handle_file_dropped(self, file_path):
        # Handle the dropped file here
        self.status.showMessage(file_path)
        self.im = io.imread(file_path)
        self.imageViewer.imv.setImage(self.im)
        self.show_message("Image successfully loaded!")

    def show_message(self, message, is_error=False):
        msg = QMessageBox()
        if is_error:
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Retry)
            msg.setWindowTitle("Error")
        else:
            msg.setWindowTitle("Info")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)

        msg.setText(message)
        msg.exec_()

# Add the following line to the end of the script to run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()
