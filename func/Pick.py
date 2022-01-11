class Pick():
    """Classe responsável por pegar a URL da tela."""

    def geturl(link: str) -> str:
        url = link.get()    # pega o texto armazenado em link
        return url
