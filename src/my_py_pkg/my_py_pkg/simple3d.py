import sys
import math
from PySide6 import QtCore, QtGui, QtWidgets, Qt3DCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Pencere Oluşturma
        self.setWindowTitle("3 Boyutlu Traktör ve Tırmık")
        self.resize(800, 600)

        # 3D Görüntüleme Alanı Oluşturma
        self.widget = QtWidgets.QWidget(self)
        self.layout = QtWidgets.QVBoxLayout(self.widget)
        self.viewer = Qt3D.Q3DWidget(self.widget)
        self.layout.addWidget(self.viewer)

        # Kamera Oluşturma
        self.camera = self.viewer.camera()
        self.camera.setPosition(QtCore.QVector3D(0, 0, 10))
        self.camera.setViewDirection(QtCore.QVector3D(0, 0, -1))

        # Traktör Oluşturma
        self.tractor = Qt3D.Q3DObject(self.viewer)
        self.tractor_mesh = Qt3D.Q3DMesh(self.tractor)
        self.tractor_mesh.setSource(QtCore.QUrl("models/tractor.obj"))

        # Tırmık Oluşturma
        self.harrow = Qt3D.Q3DObject(self.tractor)
        self.harrow_mesh = Qt3D.Q3DMesh(self.harrow)
        self.harrow_mesh.setSource(QtCore.QUrl("models/harrow.obj"))

        # Transformlar ile Traktör ve Tırmık Konumlandırma
        self.tractor_transform = Qt3D.Q3DTransform(self.tractor)
        self.tractor_transform.setTranslation(QtCore.QVector3D(0, 0, 0))
        self.harrow_transform = Qt3D.Q3DTransform(self.harrow)
        self.harrow_transform.setTranslation(QtCore.QVector3D(0, -2, 0))

        # Malzemeler ve Renkler
        self.tractor_material = Qt3D.Q3DMaterial(self.tractor)
        self.tractor_material.setDiffuse(QtCore.QColor(160, 160, 160))
        self.harrow_material = Qt3D.Q3DMaterial(self.harrow)
        self.harrow_material.setDiffuse(QtCore.QColor(200, 200, 200))

        # Animasyon Ekleme (Döndürme)
        self.rotation_animation = Qt3D.Q3DPropertyAnimation(self.tractor_transform)
        self.rotation_animation.setTargetProperty("rotation")
        self.rotation_animation.setStartValue(QtCore.QQuaternion.fromEulerAngles(0, 0, 0))
        self.rotation_animation.setEndValue(QtCore.QQuaternion.fromEulerAngles(0, 360, 0))
        self.rotation_animation.setDuration(1000)
        self.rotation_animation.setLoopCount(-1)
        self.rotation_animation.start()

        # Gösterme
        self.viewer.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
