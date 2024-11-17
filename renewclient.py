import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDesktopWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class certclient(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.FONT_FILENAME = 'SCDream7.otf'  # 폰트 파일 이름
        self.LOGO_FILENAME = 'logo.png'  # 로고 파일 이름
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

        # 로컬에서 폰트 로드
        font_id = QtGui.QFontDatabase.addApplicationFont(self.FONT_FILENAME)
        font_families = QtGui.QFontDatabase.applicationFontFamilies(font_id)

        if font_families:
            font_family = font_families[0]
            QtGui.QFontDatabase.addApplicationFont(font_family)
        else:
            font_family = 'Arial'  # 기본 폰트 설정

        # 메인 레이아웃
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # 로고
        left_widget = QtWidgets.QWidget()
        left_widget.setStyleSheet("background: url('side01.jpg') no-repeat center center; background-size: cover; border-radius: 8px;")
        main_layout.addWidget(left_widget, 1)  # 왼쪽 비율 설정

        # 왼쪽에 로고 추가
        left_layout = QVBoxLayout(left_widget)  # left_widget에 레이아웃 추가

        logo_label = QLabel(self)
        pixmap = QtGui.QPixmap(self.LOGO_FILENAME)  # 로고 이미지 로드
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(QtCore.Qt.AlignCenter)
        logo_label.setStyleSheet("border-radius: 8px;")  # 로고에 스타일 추가
        logo_label.setFixedHeight(self.height())  # 세로로 꽉 차게 설정

        # 로고를 레이아웃에 추가
        left_layout.addWidget(logo_label)
        left_layout.setContentsMargins(0, 0, 0, 0)  # 마진 없애기
        left_layout.setSpacing(0)  # 간격 없애기

        # 결과 메시지
        right_widget = QtWidgets.QWidget()
        right_widget.setStyleSheet("background-color: #1e1e1e; padding: 40px; border-radius: 8px;")
        main_layout.addWidget(right_widget, 2)  # 오른쪽 비율 설정

        right_layout = QVBoxLayout()
        right_widget.setLayout(right_layout)

        # 제목 레이블
        title_label = QLabel('파일 인증', self)
        title_label.setStyleSheet(f"font-size: 28px; color: #ffffff; margin-bottom: 20px; font-family: '{font_family}';")
        right_layout.addWidget(title_label)

        # 입력 폼
        form_layout = QVBoxLayout()
        form_layout.setSpacing(10)

        self.input_label = QLabel('발급된 키 입력:', self)
        self.input_label.setStyleSheet(f"font-size: 16px; color: #f4f4f4; font-family: '{font_family}';")
        form_layout.addWid분
        form_layout.addWidget(self.submit_button)

        self.status_label = QLabel('', self)
        self.status_label.setStyleSheet("font-size: 12px; color: #ff0000; font-family: '{font_family}';")
        form_layout.addWidget(self.status_label)

        right_layout.addLayout(form_layout)

        version_label = QLabel('V2.0.0 \nProtected By STUDIO CSGNS', self)
        version_label.setStyleSheet("font-size: 16px; color: #d1d5db; text-align: center; margin-top: auto; font-family: '{font_family}';")  # 글꼴 크기 수정
        right_layout.addWidget(version_label)

        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = certclient()
    sys.exit(app.exec_())
