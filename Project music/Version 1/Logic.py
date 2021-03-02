import pygame
from tkinter import *

class PemutarMusik():
    def __init__(self):
        self.inisialisasifile()
        self.buatTeks()
        self.buatTombolPlay()
        self.buatTombolStop()
    def inisialisasifile(self):
        self.file = 'E:\My Program\Project music\Version 1\Logic - Aquarius III.mp3'
    def putarMusik(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.file)
        pygame.mixer.music.play()
    def stopMusik(self):
        pygame.mixer.music.stop()
    def buatTeks(self):
        Label(text="logic", fg="black", bg='yellow', font='arial').pack(fil=X)
    def buatTombolStop(self):
        Button(text='stop', command=self.stopMusik).pack(fil=X)
    def buatTombolPlay(self):
        Button(text='play', command=self.putarMusik).pack(fil=X)
Tk()
PemutarMusik()
mainloop()
pygame.quit()

