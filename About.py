from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class AboutWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('About Me')
        self.setGeometry(200, 200, 350, 585)
        self.setObjectName('about_window')

        self.my_name = QLabel('Yoav Grunstein', self)
        self.my_name.setGeometry(20, 20, 310, 40)
        self.my_name.setObjectName('about_name')
        self.my_name.setAlignment(Qt.AlignCenter)

        self.my_email = QLabel('📧 yoav10g@gmail.com', self)
        self.my_email.setGeometry(20, 75, 310, 25)
        self.my_email.setObjectName('about_email')
        self.my_email.setAlignment(Qt.AlignCenter)

        self.linkedin_label = QLabel('<a href="https://www.linkedin.com/in/yoav-grunstein-095666270/" style="color: #3498db; text-decoration: none;">🔗 My LinkedIn Profile</a>', self)
        self.linkedin_label.setGeometry(20, 105, 310, 25)
        self.linkedin_label.setOpenExternalLinks(True)
        self.linkedin_label.setObjectName('about_link')
        self.linkedin_label.setAlignment(Qt.AlignCenter)

        self.github_label = QLabel('<a href="https://github.com/YoaviGreen/EXE4_IceCream" style="color: #3498db; text-decoration: none;">💻 Source code on GitHub</a>', self)
        self.github_label.setGeometry(20, 135, 310, 25)
        self.github_label.setOpenExternalLinks(True)
        self.github_label.setObjectName('about_link')
        self.github_label.setAlignment(Qt.AlignCenter)

        self.my_picture = QLabel(self)
        self.my_picture.setGeometry(35, 175, 280, 380)
        self.my_picture.setObjectName('about_picture')

        image = QPixmap("harry kane ballon d'or.jpg").scaled(264, 364)
        self.my_picture.setPixmap(image)
        self.my_picture.setAlignment(Qt.AlignCenter)


if __name__ == '__main__':
    app = QApplication()
    with open('style.qss', 'r') as f:
            app.setStyleSheet(f.read())
    window = AboutWindow()
    window.show()
    app.exec()