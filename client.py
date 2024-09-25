import sys
import requests
import os
import zipfile
import json
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDesktopWidget, QVBoxLayout, QHBoxLayout

class ZipDownloaderApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.FONT_FILENAME = 'SCDream7.otf'
        # [ REDACTED FOR SECURITY REASONS ]
        self.KEY_FILENAME = 'user_key.json'
        self.init_ui()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def init_ui(self):
        self.setWindowTitle('파일 인증')
        self.setGeometry(100, 100, 400, 200)
        self.setFixedSize(400, 200)
        self.center()

        font_id = QtGui.QFontDatabase.addApplicationFont(self.font_path)
        font_families = QtGui.QFontDatabase.applicationFontFamilies(font_id)

        if font_families:
            font_family = font_families[0]
            QtGui.QFontDatabase.addApplicationFont(font_family)
        else:
            font_family = 'Arial'


        main_layout = QVBoxLayout()

        input_layout = QHBoxLayout()
        self.input_label = QtWidgets.QLabel('발급된 키입력:', self)
        self.input_text = QtWidgets.QLineEdit(self)
        self.input_text.setPlaceholderText('여기에 키를 입력하세요')
        self.input_text.setStyleSheet("border: 1px solid #ccc; border-radius: 5px;")

        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.input_text)

        self.submit_button = QtWidgets.QPushButton('제출', self)
        self.submit_button.setStyleSheet(f"""
            QPushButton {{
                background-color: #007BFF;
                color: white;
                font-family: '{font_family}';
                font-size: 15px;
                font-weight: bold;
                border: none;
                border-radius: 5px;
                padding: 10px;
            }}
            QPushButton:hover {{
                background-color: #0056b3;
            }}
            QPushButton:pressed {{
                background-color: #004080;
            }}
        """)
        self.submit_button.clicked.connect(self.send_data_to_server)

        self.status_label = QtWidgets.QLabel('', self)
        self.status_label.setStyleSheet("font-size: 12px; color: #ff0000;")

        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.submit_button, alignment=QtCore.Qt.AlignCenter)
        main_layout.addWidget(self.status_label, alignment=QtCore.Qt.AlignCenter)

        right_label = QtWidgets.QLabel('V1.0.1', self)
        right_label.setStyleSheet("font-size: 12px; color: #333;")
        main_layout.addWidget(right_label, alignment=QtCore.Qt.AlignRight)

        self.setLayout(main_layout)

        self.setStyleSheet(f"""
            background-color: #f7f9fc; 
            font-family: '{font_family}';
        """)
        self.input_label.setStyleSheet("font-size: 14px; color: #333;")

        self.check_existing_key()

        self.show()

    def check_existing_key(self):
        # [ REDACTED FOR SECURITY REASONS ]
        pass

    def show_message(self, title, message):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec_()

    def send_data_to_server(self):
        # [ REDACTED FOR SECURITY REASONS ]
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ZipDownloaderApp()
    sys.exit(app.exec_())
