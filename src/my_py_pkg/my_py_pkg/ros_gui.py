import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2

class VideoPlayer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Pencere ayarları
        self.setWindowTitle("Rviz")
        self.setFixedSize(1280, 720)

        # Logo
        self.logo = QtGui.QPixmap("img/tas_b_with_r.png")
        self.logo_label = QtWidgets.QLabel(self)
        self.logo_label.setPixmap(self.logo.scaled(1280, 720, QtCore.Qt.KeepAspectRatio))
        self.logo_label.setAlignment(QtCore.Qt.AlignCenter)

        # Butonlar
        self.baslat_butonu = QtWidgets.QPushButton("Başlat", self)
        self.baslat_butonu.clicked.connect(self.baslat)
        self.durdur_butonu = QtWidgets.QPushButton("Durdur", self)
        self.durdur_butonu.clicked.connect(self.durdur)

        # Video oynatıcı
        self.cap = None
        self.video_frame = QtWidgets.QLabel(self)
        #self.video_frame.setStyleSheet("background-color: black")

        # Arayüz düzeni
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.logo_label)
        self.main_layout.addWidget(self.video_frame)
        self.buton_layout = QtWidgets.QHBoxLayout()
        self.buton_layout.addWidget(self.baslat_butonu)
        self.buton_layout.addWidget(self.durdur_butonu)
        self.main_layout.addLayout(self.buton_layout)
        self.setLayout(self.main_layout)

    def baslat(self):
        # Video dosyasını açma
        self.cap = cv2.VideoCapture("img/sakarya_horizontal.mp4")

        if not self.cap.isOpened():
            print("Video dosyası açılamadı!")
            return

        # Videoyu oynatma
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)

        self.logo_label.hide()

    def update_frame(self):
        # Bir kare okuma
        ret, frame = self.cap.read()
        if ret:
            # Kareyi gösterme
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(image)
            self.video_frame.setAlignment(QtCore.Qt.AlignCenter)
            self.video_frame.setPixmap(pixmap)
        else:
            # Videonun sonuna ulaşıldığında
            self.timer.stop()
            self.cap.release()
            self.video_frame.hide()
            self.logo_label.show()

    def durdur(self):
        # Videoyu durdurma ve logoyu gösterme
        if self.cap:
            self.timer.stop()
            self.cap.release()
            self.video_frame.hide()
            self.logo_label.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())
