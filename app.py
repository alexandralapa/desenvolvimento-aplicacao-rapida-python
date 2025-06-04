import tkinter as tk
from tkinter import messagebox
from conectar_db import conectar_db
from verificar_login import verificar_login
from cadastrar_usuario import cadastrar_usuario
from gerar_certificado import gerar_certificado

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Login/Cadastro")
        self.tela_login()

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def tela_login(self):
        self.limpar_tela()
        tk.Label(self.root, text="Login").pack()
        tk.Label(self.root, text="Usuário").pack()
        self.usuario_login = tk.Entry(self.root)
        self.usuario_login.pack()
        tk.Label(self.root, text="Senha").pack()
        self.senha_login = tk.Entry(self.root, show="*")
        self.senha_login.pack()
        tk.Button(self.root, text="Entrar", command=self.login).pack(pady=5)
        tk.Button(self.root, text="Cadastrar", command=self.tela_cadastro).pack()
        
    def tela_logado(self):
        self.limpar_tela()
        tk.Label(self.root, text=f"Bem-vindo, {self.nome_usuario}", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="Gerar Certificado", font=("Arial", 18)).pack(pady=10)

        tk.Label(self.root, text="Nome da palestra").pack()
        palestra_entry = tk.Entry(self.root)
        palestra_entry.pack()

        def gerar():
            nome_p = self.nome_usuario
            nome_pal = palestra_entry.get()

            if nome_p and nome_pal:
                arquivo = gerar_certificado(nome_p, nome_pal)
                messagebox.showinfo("Sucesso", f"Certificado salvo como {arquivo}")
            else:
                messagebox.showerror("Erro", "Preencha todos os campos.")

        tk.Button(self.root, text="Gerar PDF", command=gerar).pack(pady=10)
        tk.Button(self.root, text="Sair", command=self.tela_login).pack(pady=5)

        

    def tela_cadastro(self):
        self.limpar_tela()
        tk.Label(self.root, text="Cadastro").pack()
        tk.Label(self.root, text="Usuário").pack()
        self.usuario_cadastro = tk.Entry(self.root)
        self.usuario_cadastro.pack()
        tk.Label(self.root, text="Nome").pack()
        self.nome_cadastro = tk.Entry(self.root)
        self.nome_cadastro.pack()
        tk.Label(self.root, text="Senha").pack()
        self.senha_cadastro = tk.Entry(self.root, show="*")
        self.senha_cadastro.pack()
        tk.Button(self.root, text="Cadastrar", command=self.cadastrar).pack(pady=5)
        tk.Button(self.root, text="Voltar", command=self.tela_login).pack()

    def login(self):
        usuario = self.usuario_login.get()
        senha = self.senha_login.get()

        nome = verificar_login(usuario, senha)

        if nome:
            self.nome_usuario = nome  # salva o nome real
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            self.tela_logado()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    def cadastrar(self):
        usuario = self.usuario_cadastro.get()
        nome = self.nome_cadastro.get()
        senha = self.senha_cadastro.get()
        if cadastrar_usuario(usuario, nome, senha):
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            self.tela_login()
        else:
            messagebox.showerror("Erro", "Usuário já existe.")

if __name__ == "__main__":
    conectar_db()
    root = tk.Tk()
    root.geometry("350x300") 
    app = App(root)
    root.mainloop()
