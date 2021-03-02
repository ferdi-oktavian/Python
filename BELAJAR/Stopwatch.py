from tkinter import *
import time

class StopWatch(Frame):
        def __init__(self, parent):
            Frame.__init__(self, parent)
            self._start = 0.0
            self.WaktuSekarang = 0.0
            self.WaktuBerjalan = False
            self.WaktuString = StringVar()
            self.TextStart = StringVar()
            self.TextStart.set('Start')
            parent.configure(background='light blue')
            parent.title('stopwatch')
            self.buatTeks()
            self.buatKolom()
            self.buatTombol()
            self.posisi=1

        def buatTeks(self):
            self.teks=Label(self, textvariable=self.waktuString,font="Verdana 19 bold", bg ='light', fg ='blue' )
            self.aturWaktu(self.WaktuSekarang)
            self.teks.grid(row=0, column=0)

        def perbarui(self):
            self.WaktuSekarang = time.time() - self._start
            self.aturWaktu(self.Waktusekarang)
            self._timer = self.after(50,self.perbarui)
