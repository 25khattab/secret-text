from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QPushButton
import sys
import steganography

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 600, 400)
        self.setFixedSize(600, 400)
        self.set_window()
        self.setWindowTitle("Steganography")
        self.show()

    def set_window(self):
        encode_btn = QPushButton("encode", self)
        encode_btn.move(150, 30)
        encode_btn.clicked.connect(self.encode)
        decode_btn = QPushButton("decode", self)
        decode_btn.move(350, 30)
        decode_btn.clicked.connect(self.decode)
        self.text_box = QPlainTextEdit(self)
        self.text_box.setGeometry(0, 70, 600, 300)

    def encode(self):
        image = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Select Image to encode', "Image Files (*.jpg *.gif *.bmp *.png)")
        data = self.text_box.toPlainText()
        newImg = QtWidgets.QFileDialog.getSaveFileName(
            self, 'Save the picture')
        steganography.encode(image[0], data, newImg[0])

    def decode(self):
        image = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Select Image to decode', "Image Files (*.jpg *.gif *.bmp *.png)")
        text = steganography.decode(image[0])
        self.text_box.setPlainText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
