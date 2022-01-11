from func.Procedimentos import Procedimentos
from tkinter import *


def tela():
    """Função responsável pela interface gráfica."""

    # estrutura padrão
    root = Tk()
    root.title("Baixar Youtube")
    root.geometry("400x200+800+80")
    root.resizable(False, False)
    global link
    link = StringVar()  # variável que será puxada

    # Widgets
    faixa1 = Frame(root,
                   bg="#111111",
                   width=500,
                   height=150).place(x=0, y=0)
    faixa2 = Frame(root,
                   bg="#080808",
                   width=500,
                   height=80).place(x=0, y=130)
    inicio = Label(faixa1,
                   foreground="white",
                   background="#111111",
                   font="impact 20 ",
                   text="Baixar músicas youtube").place(x=65, y=10)
    mensagem = Label(faixa1,
                     foreground="white",
                     background="#111111",
                     font="calibri",
                     text="Insira a url do vídeo:").place(x=15, y=65)

    puxarurl = Entry(root,
                     width=60,
                     textvariable=link).place(x=18, y=90)

    download = Button(root,
                      width=10,
                      height=2,
                      text="Download",
                      font=10,
                      anchor="center",
                      command=lambda: Procedimentos.baixar(link)).place(x=30, y=140)

    transmitirbt = Button(root,
                          width=10,
                          height=2,
                          text="Transmitir",
                          font=10,
                          anchor="center",
                          command=lambda: Procedimentos.transmitir(link)).place(x=270, y=140)
    root.mainloop()
