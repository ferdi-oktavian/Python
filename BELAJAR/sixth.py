import pygame
from tkinter import *
class PemutarMusik():
    def __init__(self):
        self.inialisasifile()
        self.buatTeks()
        self.buatTombolPlay()
        self.buatTombolStop()
    def inialisasifile(self):
        self.file = 'Logic - Confessions of a Dangerous Mind'
    def putarMusik(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.file)
        pygame.mixer.music.play()
    def stopmusik(self):
        pygame.mixer.music.stop()
    def buatTeks(self):
        Label(text = 'logic' ,fg='red', bg='blue', font='verdana 10 bold').pack(fill=X)
    def buatTombolStop(self):
        Button(text='stop',command = self.stopmusik).pack(fill=X)
    def buatTombolPlay(self):
        Button(text = 'play',command = self.putarMusik).pack(fill = X)
Tk()
PemutarMusik()
mainloop()
pygame.quit()