import pygame
from tkinter import * 
from tkinter import Tk, filedialog,END
import os

class PemutarMusik(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        parent.geometry('1920x1080')
        self.parent = parent
        self.nama = StringVar()
        self.nama.set('open the file')
        self.buatTeks()
        self.buatTombolStop()
        self.buatOpen()
        self.buatTombolPlay()
    def inisialisasiFile(self,file):
        self.file = file
    def PutarMusik(self):
        try:
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(self.file)
            pygame.mixer.music.play()
        except:
            pass
    def stopMusik(self):
        try:
            pygame.mixer.music.stop()
        except:
            pass
    def buatTeks(self):
        Label(textvariable=self.nama,fg='red',bg='green',font='calibri').pack(fill=X)
    def buatTombolStop(self):
        Button(text='stop',command=self.stopMusik).pack(fill=X)
    def buatOpen(self):
        Button(text='Open',command=self.bukaFile).pack(fill=X)
    def buatTombolPlay(self):
        Button(text='Play',command=self.PutarMusik).pack(fill=X)
    def bukaFile(self):
        TipeFile = [('E:\My Program\Project music\Verison 2\Drake - Toosie Slide.mp3','Drake - Toosie Slide'),('All files',('*'))]
        bukaFile = filedialog.Open(self,filetypes=TipeFile)
        bukaFile.show()
        try:
            file=bukaFile.filename
            self.inisialisasiFile(file)
            self.nama.set(os.path.basename(file))
        except:
            pass
root=Tk()
PemutarMusik(root)
mainloop()
pygame.quit()