"""Projeto para estudo de Web Scrapping.

    Feito por Kauã Vinícius Ponte Aguiar, aluno da 
    Universidade de Brasília - UnB, com a finalidade 
    de utilizar a biblitoeca youtude_dl para realizar 
    o download do arquivo de audio de algum vídeo no
    youtube.
    Problemas: O app trava quando está realizando o 
    download do arquivo mp3.
    Há arquivos que ainda não são exportados na função 
    transmitir.
    """

# importar bibliotecas
import shutil
import youtube_dl
from tkinter import *
import os

# puxar string do entry


def geturl(link):
    url = link.get()
    return url

# tirar o arquivo de dentro da pasta mp3 e coloca-lo em uma pasta
# na área de trabalho


def transmitir(link):
    obj = geturl(link)

    # procedimentos padrões da yt_dl para obter um objeto transmitítir
    ydl_opts = {
        'format': "bestaudio/best",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(obj, download=False)

        natural = r"C:\\Users\\PC\\Desktop\\Programas\\Pegarlinketocar" + \
            "\\" + info['title'] + '-' + info["id"] + ".webm"
        destino = r"C:\\Users\\PC\\Desktop\\Musicas\\"

        try:
            os.mkdir(destino)
        except FileExistsError:
            pass
        shutil.move(natural, destino)


def baixar(link):
    url = geturl(link)
    ydl_opts = {
        'format': "bestaudio/best",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        mp3 = ydl.download([url])


def main():
    root = Tk()
    root.title("Baixar Youtube")
    root.geometry("400x200+800+80")
    root.resizable(False, False)
    global link
    link = StringVar()

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
                      command=lambda: baixar(link)).place(x=30, y=140)

    transmitirbt = Button(root,
                          width=10,
                          height=2,
                          text="Transmitir",
                          font=10,
                          anchor="center",
                          command=lambda: transmitir(link)).place(x=270, y=140)
    root.mainloop()


if __name__ == '__main__':
    main()
