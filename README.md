# 🔐 Sistema de Criptografia AES

Um sistema simples e robusto para **criptografia e descriptografia de arquivos** usando **AES-256 em modo CFB**.  
Ideal para proteger informações sensíveis em arquivos de texto ou outros formatos.

---

## ✨ Funcionalidades

- Criptografa arquivos com **AES-256** (seguro e confiável).  
- Descriptografa arquivos desde que a senha correta seja fornecida.  
- Cria automaticamente as pastas necessárias no **Desktop** caso não existam.  
- Interface em linha de comando (CLI) simples e intuitiva.  
- Código modular, seguindo boas práticas do **PEP 8** e **PEP 257**.  

---

## 📂 Estrutura do Projeto

```

.
├── crypto\_utils.py   # Funções de criptografia e descriptografia
├── file\_utils.py     # Funções auxiliares de manipulação de arquivos/pastas
├── config.py         # Configurações de nomes de pastas
├── main.py           # Menu principal do sistema
├── requirements.txt  # Dependências do projeto
└── README.md         # Documentação

````

---

## ⚙️ Requisitos

- Python **3.8+**

Instale as dependências com:

```bash
pip install -r requirements.txt
````

---

## ▶️ Como Usar

### 1. Clone o repositório

```bash
git clone https://github.com/Iannobres/Projeto-Backup-Arquivos-Seguros.git
cd Projeto-Backup-Arquivos-Seguros
```

### 2. Instale os requisitos

```bash
pip install -r requirements.txt
```

### 3. Execute o programa

```bash
python main.py
```

### 4. Escolha uma opção no menu

```
=== Sistema de Criptografia AES ===

1 - Criptografar arquivo
2 - Descriptografar arquivo
3 - Sair
```

---

## 🔑 Exemplo de Uso

### 🔒 Criptografar um arquivo

* Digite uma senha para proteger o arquivo.
* Informe a pasta com o arquivo original (ou deixe vazio para usar a pasta padrão no Desktop).
* Escolha a pasta para salvar o backup criptografado (ou deixe vazio para usar a pasta padrão).
* Informe o nome do arquivo (sem precisar colocar a extensão).
* O arquivo será salvo como `.enc` na pasta de backup.

### 🔓 Descriptografar um arquivo

* Digite a mesma senha usada na criptografia.
* Informe a pasta do backup criptografado (ou deixe vazio).
* Escolha a pasta onde o arquivo restaurado será salvo.
* Informe o nome do arquivo `.enc` e o nome que deseja dar ao arquivo restaurado.
* O arquivo original será recuperado na pasta de restauração.

---

## ⚠️ Observações Importantes

* Cada arquivo é protegido pela senha digitada no momento da criptografia.
* **Se a senha for perdida, não será possível recuperar o arquivo.**
* Apenas arquivos criptografados com este sistema podem ser restaurados corretamente.

---

## 📜 Licença

Este projeto é distribuído sob a licença **MIT**.
Sinta-se à vontade para usar, modificar e compartilhar.
