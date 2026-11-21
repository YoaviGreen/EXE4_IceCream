from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from About import AboutWindow

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.about_window = AboutWindow()

        self.temperatures = []
        self.revenues = []

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ice Cream Revenue')
        self.setGeometry(100, 100, 820, 640)

        self.choose_button = QPushButton('Choose File', self)
        self.choose_button.setGeometry(20, 20, 140, 35)

        self.file_label = QLabel('Selected file:', self)
        self.file_label.setGeometry(180, 20, 100, 35)

        self.file_box = QLineEdit(self)
        self.file_box.setGeometry(285, 20, 380, 35)
        self.file_box.setReadOnly(True)
        self.file_box.setObjectName('output')
        self.file_box.setPlaceholderText('No file selected')

        self.about_button = QPushButton('About', self)
        self.about_button.setGeometry(685, 20, 115, 35)
        self.about_button.clicked.connect(self.show_about_window)
        
        self.figure = Figure()
        self.ax = self.figure.add_subplot(1, 1, 1)
        self.ax.set_title('Choose a file to see the graph')

        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.setParent(self)
        self.canvas.setGeometry(20, 120, 780, 500)

        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.toolbar.setGeometry(20, 70, 780, 40)

    def show_about_window(self):
        self.about_window.show()


if __name__ == '__main__':
    app = QApplication()
    with open('style.qss', 'r') as f:
        app.setStyleSheet(f.read())
    window = MainWindow()
    window.show()
    app.exec()