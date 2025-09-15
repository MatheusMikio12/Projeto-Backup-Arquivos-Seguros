from Crypto.Cipher import AES
import os

from Crypto.Cipher import AES
import os

def criptografar_arquivo(entrada: str, saida: str, filename: str, key: bytes) -> None:
    """
    Criptografa um arquivo usando AES-256 em modo CFB.

    Args:
        entrada (str): Caminho da pasta contendo o arquivo original.
        saida (str): Caminho da pasta onde o arquivo criptografado será salvo.
        filename (str): Nome do arquivo original (com extensão).
        key (bytes): Chave AES gerada a partir da senha do usuário.

    Returns:
        None
    """
    entrada_path = os.path.join(entrada, filename)
    saida_path = os.path.join(saida, filename + ".enc")

    with open(entrada_path, 'rb') as f:
        plaintext = f.read()

    cipher = AES.new(key, AES.MODE_CFB)
    ciphertext = cipher.encrypt(plaintext)

    with open(saida_path, 'wb') as f:
        f.write(cipher.iv + ciphertext)

    print(f"\n[OK] Arquivo criptografado salvo em: {saida_path}")


def descriptografar_arquivo(entrada: str, saida: str, enc_filename: str, key: bytes, output_filename: str) -> None:
    """
    Descriptografa um arquivo criptografado com AES-256 em modo CFB.

    Args:
        entrada (str): Caminho da pasta contendo o arquivo criptografado.
        saida (str): Caminho da pasta onde o arquivo restaurado será salvo.
        enc_filename (str): Nome do arquivo criptografado (com extensão .enc).
        key (bytes): Chave AES gerada a partir da senha do usuário.
        output_filename (str): Nome do arquivo de saída restaurado.

    Returns:
        None
    """
    entrada_path = os.path.join(entrada, enc_filename)
    saida_path = os.path.join(saida, output_filename)

    with open(entrada_path, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    plaintext = cipher.decrypt(ciphertext)

    with open(saida_path, 'wb') as f:
        f.write(plaintext)

    print(f"[OK] Arquivo restaurado em: {saida_path}")