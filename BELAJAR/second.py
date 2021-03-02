from tkinter import *
import time

class StopWatch(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self._start = 0.0
        self.waktuSekarang = 0.0
        self.sedangBerjalan = False
        self.waktuString = StringVar()
        self.textStart= StringVar()
        self.textStart.set('Start')
        parent.configure(background='light blue')
        parent.title('stopwatch')
        self.buatTeks()
        self.buatTombol()

    def buatTeks(self):
        self.teks = Label(self, textvariable=self.waktuString,font="Verdana 19 bold", bg='light blue', fg='blue')
        self.aturWaktu(self.waktuSekarang)
        self.teks.grid(row=0, column=0)

    def perbarui(self):
        self.waktuSekarang = time.time() - self._start
        self.aturWaktu(self.waktuSekarang)
        self._timer = self.after(50, self.perbarui)

    def aturWaktu(self, waktu):
        menit = int(waktu / 60)
        detik = int(waktu - menit * 60.0)
        jam = int((waktu - menit * 60.0 - detik) * 100)
        self.waktuString.set('%02d:%02d:%02d' % (menit, detik, jam))

    def Start(self):
        if not self.sedangBerjalan and (self.textStart.get() == 'Start' or self.textStart.get()=='Resume') :
            self.textStart.set('Pause')
            self._start = time.time() - self.waktuSekarang
            self.perbarui()
            self.sedangBerjalan = True
        elif self.sedangBerjalan and self.textStart.get() == 'Pause' :
            self.textStart.set('Resume')
            self.pause()

    def pause(self):
        if self.sedangBerjalan:
            self.after_cancel(self._timer)
            self.waktuSekarang = time.time() - self._start
            self.aturWaktu(self.waktuSekarang)
            self.sedangBerjalan = False

    def buatTombol(self):
        Button(textvariable=self.textStart, command=self.Start).grid(row=2, column=1)

def main():
    root = Tk()
    sw = StopWatch(root)
    sw.grid(row=0,column=0, columnspan=4)
    root.mainloop()

if __name__ == '__main__':
    main()