import os
import sqlite3
import threading
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from contas import Contas
from dados import Dados

class interface(Contas, Dados):
    def __init__(self, tela):

        self.frame_mestre = LabelFrame(tela, padx=0, pady=0)
        self.frame_mestre.pack(padx=200, pady=100)

        self.teste = Button(self.frame_mestre, text='Executar', command=self.relatorio_inicial)
        self.teste.pack()



if __name__ == '__main__':
    tela = Tk()
    objeto_tela = interface(tela)
    tela.resizable(1, 1)
    #tela.title()
    #tela.config(menu=objeto_tela.menu_certidões)
    tela.mainloop()
