import tkinter as tk
import datetime

class TelaPrincipal:
    def __init__(self, master):
        self.nossaTela = master
        self.lblRelogio = tk.Label
            (self.nossaTela, font=('Calibri', 26), fg='Purple')
        self.lblRelogio.pack(pady=30, pdx=30)
        self.alteracao()

        def alteracao(self):
          now = datetime.datetime.now()
          self.lblRelogio['text'] = now.strftime('%H:%M:%S')
          self.nossaTela.after(1000, self.alteracao)

janelaRaiz = tk.Tk()
TelaPrincipal(janelaRaiz)
janelaRaiz.mainloop()
