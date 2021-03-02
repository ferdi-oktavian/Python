import pygame
from tkinter import *
class PemutarMusik():
    def __init__(self):
        self.inisialisasifile()
        self.buatTeks()
        self.buatTombolPlay()
        self.buatTombolStop()
    def inisialisasifile(self):
        self.file = "Logic - Icy (feat. Gucci Mane) (Official Audio)"
    def putarMusik(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.file)
        pygame.mixer.music.play()
    def stopMusik(self):
        pygame.mixer.music.stop()
    def buatTeks(self):
        Label(text="ICY ", fg='blue', bg='black', font='Verdana 10 bold').pack(fill=X)
    def buatTombolStop(self):
        Button(text="Stop", command=self.stopMusik).pack(fill=X)
    def buatTombolPlay(self):
        Button(text="Play", command=self.putarMusik).pack(fill=X)
Tk()
PemutarMusik()
mainloop()
pygame.quit()