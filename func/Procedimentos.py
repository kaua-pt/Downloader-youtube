import shutil
import youtube_dl
import os
from .Pick import Pick
import tkinter


class Procedimentos():
    """Classe para armazenar os procedimentos do programa."""

    def transmitir(link: str) -> None:
        """Função com a finalizade de transmitir o arquivo de música para a pasta padrão."""
        obj: str = Pick.geturl(link)

        # paths
        natural = r"C:\\Users\\PC\\Desktop\\Programas\\Pegarlinketocar\\dist\\"
        destino = r"C:\\Users\\PC\\Desktop\\Musicas\\"

        try:
            os.mkdir(destino)  # se o arquivo não exitir, ele o cria

        except FileExistsError:
            pass

        files = os.listdir(natural)  # lista todos os arquivos em natural

        for file in files:
            if file != "main.exe":  # como o arquivo de música vai para dist, se o arquivo não for main .exe, ele move o arquivo
                shutil.move(natural + file, destino)

    def baixar(link: str, root) -> None:
        """Procedimento para baixar a música."""

        root.update()

        url: str = Pick.geturl(link)
        # opções para baixar em arquivo de audio
        ydl_opts = {
            'format': "bestaudio/best",
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        root.update()
