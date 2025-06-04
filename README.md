# 🧾 Aplicação de Login e Geração de Certificados

Esta é uma aplicação desktop simples feita com **Python** e **Tkinter**, que permite o cadastro e login de usuários, além da geração de certificados em PDF com o nome da pessoa e da palestra.

## 📦 Requisitos

- Python 3.10 ou superior
- Pip (gerenciador de pacotes do Python)

## ⚙️ Como rodar

1. **Clone o projeto ou baixe os arquivos**

2. **Crie e ative um ambiente virtual (opcional, mas recomendado)**

```bash
python3 -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate
```
3. **Instale as dependências necessárias
O Tkinter é a biblioteca padrão do Python para interfaces gráficas. Na maioria das instalações do Python, ele já vem embutido. Mas se não estiver, siga as instruções abaixo para instalar manualmente:

- No Linux 
```bash
sudo apt update
sudo apt install python3-tk
```
Após isso, instale os requirements da aplicação
```bash
pip install -r requirements
```
4. **Execute o programa**
```bash
python3 app.py
```

## 💡 Funcionalidades ##

- Cadastro de usuário com nome, usuário e senha (criptografada com hash)
- Login com verificação segura
- Geração de certificados personalizados em PDF
- Interface gráfica amigável (Tkinter)
- Banco de dados local SQLite





