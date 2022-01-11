import shutil
import youtube_dl
import os
from .Pick import Pick


class Procedimentos():
    """Classe para armazenas os procedimentos realizados no app."""

    def transmitir(link: str) -> None:
        """Função com a finalizade de transmitir o arquivo de música para a pasta padrão."""

        obj: str = Pick.geturl(link)

        with youtube_dl.YoutubeDL() as ydl:
            info = ydl.extract_info(obj, download=False)

            # paths
            natural = r"C:\Users\PC\Desktop\Programas\Pegarlinketocar\dist" + \
                "\\" + info['title'] + '-' + info["id"] + \
                "." + info['requested_formats'][1]['ext']

            destino = r"C:\\Users\\PC\\Desktop\\Musicas\\"

            try:
                os.mkdir(destino)
            except FileExistsError:
                pass

            # mover para a pasta destino que está na área de trabalho
            shutil.move(natural, destino)

    def baixar(link: str) -> None:
        """Procedimento para baixar a música."""

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
