from PySide import QtGui, QtCore
from PySide.phonon import Phonon
import sys

class PemutarMusik(QtGui.QMainWindow) :
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.inisialisasiMedia()
        self.buatTombol()
        self.buatTeks()
        self.layout()
        self.susunTombol()
        self.rangkai()

        self.connect(self.pemutar, QtCore.SIGNAL('stateChanged(Phonon::State, Phonon::State)'), self.statusBerubah)

        self.putarMusik()

    def inisialisasiMedia(self):
        self.suara = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.pemutar = Phonon.MediaObject(self)

        Phonon.createPath(self.pemutar, self.suara)

    def buatTombol(self):
        self.tombolWeb = QtGui.QAction(self.style().standardIcon(QtGui.QStyle.SP_ComputerIcon), "Pergi Ke Web", self, triggered=self.perintahWeb)

    def perintahWeb(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('Http://mn-belajarpython.blogspot.co.id'))

    def closeEvent(self, event):
        self.destroy()

    def buatTeks(self):
        self.indikator = QtGui.QLabel(''' mn-belajarpython.blogspot.co.id ''')

    def layout(self):
        widgetTengah = QtGui.QWidget()
        self.layoutUtama = QtGui.QVBoxLayout(widgetTengah)
        self.layoutTombol = QtGui.QToolBar()

        self.layoutTombol.setMovable(False)
        self.layoutUtama.setSpacing(0)
        self.setCentralWidget(widgetTengah)

    def susunTombol(self):
        self.layoutTombol.addAction(self.tombolWeb)
        self.layoutTombol.addSeparator()
        self.layoutTombol.addWidget(QtGui.QLabel("  "))
        self.layoutTombol.addWidget(self.indikator)

    def rangkai(self):
        self.addToolBar( QtCore.Qt.BottomToolBarArea ,self.layoutTombol)

    def putarMusik(self):
        self.pemutar.setCurrentSource('./hysteria.mp3')
        self.pemutar.play()


    def statusBerubah(self, statusBaru, oldState):
        if statusBaru == Phonon.ErrorState:
            if self.mediaObject.errorType() == Phonon.FatalError:
                QtGui.QMessageBox.warning(self, self.tr("Fatal Error"), self.mediaObject.errorString())
            else:
                QtGui.QMessageBox.warning(self, self.tr("Error"), self.mediaObject.errorString())


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = PemutarMusik()
    window.setWindowTitle("Musik Player -> mn-belajarpython.blogspot.co.id")
    window.show()
    sys.exit(app.exec_())