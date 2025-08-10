import customtkinter as ctk

# Configurações do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Criar a janela principal
janela = ctk.CTk()
janela.geometry("400x300")
janela.title("Teste Banco")

# Adicionar um texto
label = ctk.CTkLabel(janela, text="Olá, Cliente!", font=("Arial", 20))
label.pack(pady=20)

# Botão para fechar
botao = ctk.CTkButton(janela, text="Fechar", command=janela.destroy)
botao.pack(pady=10)

# Mantém a janela aberta
janela.mainloop()
