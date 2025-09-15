from criptografar_utils import criptografar_arquivo, descriptografar_arquivo
from arquivo_utils import garantir_pasta, adicionar_extensao_arquivo
import hashlib

def main() -> None:
    """
    Função principal do sistema de criptografia.
    Gerencia o menu de opções e controla o fluxo do programa.

    Opções disponíveis:
        1 - Criptografar arquivo
        2 - Descriptografar arquivo
        3 - Sair

    Returns:
        None
    """
    while True:
        print("\n=== Sistema de Criptografia AES ===")
        print("1 - Criptografar arquivo")
        print("2 - Descriptografar arquivo")
        print("3 - Sair")
        print("=====================================")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "3":
            print("\nSaindo do programa...")
            break

        try:
            if escolha == "1":
                senha = input("\nDigite uma senha para encriptografar: ").strip()
                entrada = input("Caminho da pasta de arquivos originais (ou deixe vazio): ").strip()
                saida = input("Caminho da pasta para salvar o backup criptografado (ou deixe vazio): ").strip()

                entrada = garantir_pasta(entrada, "Arquivos Originais")
                saida = garantir_pasta(saida, "Arquivos Criptografados")

                arquivo = input("\nNome do arquivo a criptografar: ").strip()
                arquivo = adicionar_extensao_arquivo(arquivo, ".txt")

                key = hashlib.sha256(senha.encode()).digest()
                criptografar_arquivo(entrada, saida, arquivo, key)

            elif escolha == "2":
                senha = input("\nDigite a senha usada na criptografia: ").strip()
                entrada = input("Caminho da pasta do backup criptografado (ou deixe vazio): ").strip()
                saida = input("Caminho da pasta para salvar os arquivos restaurados (ou deixe vazio): ").strip()

                entrada = garantir_pasta(entrada, "Arquivos Criptografados")
                saida = garantir_pasta(saida, "Arquivos Restaurados")

                arquivo_enc = input("\nNome do arquivo criptografado: ").strip()
                arquivo_enc = adicionar_extensao_arquivo(arquivo_enc, ".txt.enc")

                arquivo_out = input("Nome do arquivo restaurado: ").strip()
                arquivo_out = adicionar_extensao_arquivo(arquivo_out, ".txt")

                key = hashlib.sha256(senha.encode()).digest()
                descriptografar_arquivo(entrada, saida, arquivo_enc, key, arquivo_out)

            else:
                print("\nOpção inválida! Tente novamente.")

        except Exception as e:
            print(f"[ERRO] Ocorreu um problema: {e}")

if __name__ == "__main__":
    main()
