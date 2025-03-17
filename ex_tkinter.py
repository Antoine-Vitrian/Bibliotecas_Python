from tkinter import Tk, Button, Label

def dizer_ola():
    rotulo_ola_mundo.config(text = "Olá mundo!")

janela = Tk()
janela.title("Dizer olá!")    

botao_dizer_ola = Button(janela, text = "Dizer olá!", command=dizer_ola)
botao_dizer_ola.pack()

rotulo_ola_mundo = Label(janela, text="")
rotulo_ola_mundo.pack()

janela.mainloop()

