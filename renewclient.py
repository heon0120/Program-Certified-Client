import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDesktopWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QProgressBar

class CertClient(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def init_ui(self):
        self.setWindowTitle('파일 인증')
        self.setGeometry(100, 100, 800, 500)
        self.setFixedSize(800, 500)
        self.center()

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(200, 400, 400, 25)
        self.progress_bar.setValue(0)
        self.progress_bar.setVisible(False)

        font_id = QtGui.QFontDatabase.addApplicationFont('SCDream7.otf')
        font_families = QtGui.QFontDatabase.applicationFontFamilies(font_id)
        font_family = font_families[0] if font_families else 'Arial'

        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        left_widget = QtWidgets.QWidget()
        left_widget.setStyleSheet(
            "background: url('side01.jpg') no-repeat center center; background-size: cover; border-radius: 10px;")
        main_layout.addWidget(left_widget, 1)

        left_layout = QVBoxLayout(left_widget)
        logo_label = QLabel(self)
        pixmap = QtGui.QPixmap('logo.png')
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(QtCore.Qt.AlignCenter)
        logo_label.setStyleSheet("border-radius: 10px;")
        logo_label.setFixedHeight(int(self.height() * 0.4))
        left_layout.addWidget(logo_label)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(0)

        right_widget = QtWidgets.QWidget()
        right_widget.setStyleSheet("background-color: #2C2F33; border-radius: 10px; padding: 40px;")
        main_layout.addWidget(right_widget, 2)

        right_layout = QVBoxLayout()
        right_widget.setLayout(right_layout)

        title_label = QLabel('파일 인증', self)
        title_label.setStyleSheet(
            f"font-size: 32px; color: #FFFFFF; margin-bottom: 20px; font-family: '{font_family}';")
        right_layout.addWidget(title_label)

        form_layout = QVBoxLayout()
        form_layout.setSpacing(20)

        self.input_label = QLabel('발급된 키 입력:', self)
        self.input_label.setStyleSheet(f"font-size: 18px; color: #FFFFFF; font-family: '{font_family}';")
        form_layout.addWidget(self.input_label)

        self.input_text = QLineEdit(self)
        self.input_text.setPlaceholderText('여기에 키를 입력하세요')
        self.input_text.setFixedHeight(40)
        self.input_text.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                border: 1px solid #DDDDDD;
                border-radius: 8px;
                padding: 10px;
                font-size: 16px;
            }
            QLineEdit:focus {
                border: 1px solid #007BFF;
                box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
            }
        """)
        form_layout.addWidget(self.input_text)

        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setAlignment(QtCore.Qt.AlignRight)

        self.submit_button = QPushButton('제출', self)
        self.submit_button.setFixedHeight(30)
        self.submit_button.setFixedWidth(100)
        self.submit_button.setStyleSheet(f"""
            QPushButton {{
                background-color: #007BFF;
                color: white;
                font-size: 16px;
                border: none;
                border-radius: 8px;
                padding: 8px 20px;
                font-family: '{font_family}';
                transition: background-color 0.3s, transform 0.2s;
            }}
            QPushButton:hover {{
                background-color: #0056b3;
            }}
            QPushButton:pressed {{
                background-color: #004085;
                transform: scale(0.95);
            }}
        """)
        button_layout.addWidget(self.submit_button)
        form_layout.addLayout(button_layout)

        self.status_label = QLabel('', self)
        self.status_label.setStyleSheet("font-size: 14px; color: #FF5656;")
        form_layout.addWidget(self.status_label)

        right_layout.addLayout(form_layout)

        version_label = QLabel('V2.0.0 \nProducted By TEAM ARON', self)
        version_label.setStyleSheet(
            "font-size: 12px; color: #B9BBBE; text-align: center; margin-top: auto;")
        right_layout.addWidget(version_label)

        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CertClient()
    sys.exit(app.exec_())
