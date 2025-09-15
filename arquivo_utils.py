import os

def get_desktop() -> str:
    """
    Retorna o caminho absoluto do Desktop do usuário.

    Returns:
        str: Caminho para a pasta Desktop.
    """
    return os.path.join(os.path.expanduser("~"), "Desktop")


def garantir_pasta(caminho: str, nome_padrao: str) -> str:
    """
    Garante que a pasta exista. Caso não exista, cria a pasta no Desktop.

    Args:
        caminho (str): Caminho da pasta desejada.
        nome_padrao (str): Nome da pasta padrão a ser criada no Desktop se o caminho não existir.

    Returns:
        str: Caminho final da pasta garantida.
    """
    if not caminho or not os.path.exists(caminho):
        caminho = os.path.join(get_desktop(), nome_padrao)
        os.makedirs(caminho, exist_ok=True)
        print(f"[INFO] Pasta '{nome_padrao}' criada no Desktop: {caminho}")
    return caminho


def adicionar_extensao_arquivo(nome: str, extensao_padrao: str) -> str:
    """
    Adiciona uma extensão ao arquivo caso ele não possua uma.

    Args:
        nome (str): Nome do arquivo informado pelo usuário.
        extensao_padrao (str): Extensão padrão a ser adicionada.

    Returns:
        str: Nome do arquivo com a extensão garantida.
    """
    if not os.path.splitext(nome)[1]:
        nome += extensao_padrao
    return nome