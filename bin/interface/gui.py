# interface/gui.py
import customtkinter as ctk
from models.banco import Banco

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self, banco: Banco):
        super().__init__()
        self.banco = banco
        self.title("Banco - App")
        self.geometry("800x450")
        self._build_ui()

    def _build_ui(self):
        # frame lateral com botões
        frame_left = ctk.CTkFrame(self, width=220)
        frame_left.pack(side="left", fill="y", padx=12, pady=12)

        ctk.CTkLabel(frame_left, text="Menu", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(4,12))

        ctk.CTkButton(frame_left, text="Criar Usuário", command=self._open_criar_usuario).pack(fill="x", pady=6)
        ctk.CTkButton(frame_left, text="Nova Conta", command=self._open_criar_conta).pack(fill="x", pady=6)
        ctk.CTkButton(frame_left, text="Depositar", command=self._open_depositar).pack(fill="x", pady=6)
        ctk.CTkButton(frame_left, text="Sacar", command=self._open_sacar).pack(fill="x", pady=6)
        ctk.CTkButton(frame_left, text="Extrato", command=self._open_extrato).pack(fill="x", pady=6)
        ctk.CTkButton(frame_left, text="Listar Contas", command=self._open_listar_contas).pack(fill="x", pady=6)
        ctk.CTkButton(frame_left, text="Sair", command=self.destroy, fg_color="tomato").pack(fill="x", pady=(20,6))

        # área principal para mostrar mensagens/retorno
        self.output = ctk.CTkTextbox(self, width=520, height=380)
        self.output.pack(padx=12, pady=12, expand=True, fill="both")
        self._log("Aplicação iniciada. Use o menu à esquerda.")

    def _log(self, text: str):
        self.output.configure(state="normal")
        self.output.insert("end", text + "\n\n")
        self.output.see("end")
        self.output.configure(state="disabled")

    # ---------- janelas / diálogos ----------
    def _open_criar_usuario(self):
        win = ctk.CTkToplevel(self)
        win.title("Criar Usuário")
        win.geometry("400x280")
        nome = ctk.CTkEntry(win, placeholder_text="Nome completo")
        nome.pack(pady=8, padx=12)
        data_nasc = ctk.CTkEntry(win, placeholder_text="Data de nascimento (dd-mm-aaaa)")
        data_nasc.pack(pady=8, padx=12)
        cpf = ctk.CTkEntry(win, placeholder_text="CPF (somente números)")
        cpf.pack(pady=8, padx=12)
        endereco = ctk.CTkEntry(win, placeholder_text="Endereço")
        endereco.pack(pady=8, padx=12)

        def criar():
            c = cpf.get().strip()
            if not c.isdigit() or len(c) != 11:
                self._log("CPF inválido. Deve ter 11 dígitos.")
                return
            ok, msg = self.banco.criar_usuario(nome.get().strip(), data_nasc.get().strip(), c, endereco.get().strip())
            self._log(msg)
            win.destroy()

        ctk.CTkButton(win, text="Criar", command=criar).pack(pady=12)

    def _open_criar_conta(self):
        win = ctk.CTkToplevel(self)
        win.title("Criar Conta")
        win.geometry("360x180")
        cpf = ctk.CTkEntry(win, placeholder_text="CPF do titular (11 dígitos)")
        cpf.pack(pady=12, padx=12)

        def criar():
            c = cpf.get().strip()
            if not c.isdigit() or len(c) != 11:
                self._log("CPF inválido.")
                return
            conta, msg = self.banco.criar_conta(c)
            if conta:
                self._log(f"{msg} - Número da conta: {conta.numero_conta}")
            else:
                self._log(msg)
            win.destroy()

        ctk.CTkButton(win, text="Criar Conta", command=criar).pack(pady=8)

    def _open_depositar(self):
        win = ctk.CTkToplevel(self)
        win.title("Depositar")
        win.geometry("360x200")
        num = ctk.CTkEntry(win, placeholder_text="Número da conta")
        num.pack(pady=8, padx=12)
        valor = ctk.CTkEntry(win, placeholder_text="Valor (ex: 120.50)")
        valor.pack(pady=8, padx=12)

        def confirmar():
            try:
                n = int(num.get().strip())
                v = float(valor.get().strip())
            except Exception:
                self._log("Erro: número da conta ou valor inválido.")
                return
            ok, msg = self.banco.depositar(n, v)
            self._log(msg)
            win.destroy()

        ctk.CTkButton(win, text="Confirmar", command=confirmar).pack(pady=12)

    def _open_sacar(self):
        win = ctk.CTkToplevel(self)
        win.title("Sacar")
        win.geometry("360x220")
        num = ctk.CTkEntry(win, placeholder_text="Número da conta")
        num.pack(pady=8, padx=12)
        valor = ctk.CTkEntry(win, placeholder_text="Valor")
        valor.pack(pady=8, padx=12)

        def confirmar():
            try:
                n = int(num.get().strip())
                v = float(valor.get().strip())
            except Exception:
                self._log("Erro: número da conta ou valor inválido.")
                return
            ok, msg = self.banco.sacar(n, v)
            self._log(msg)
            win.destroy()

        ctk.CTkButton(win, text="Confirmar Saque", command=confirmar).pack(pady=12)

    def _open_extrato(self):
        win = ctk.CTkToplevel(self)
        win.title("Extrato")
        win.geometry("500x400")
        num = ctk.CTkEntry(win, placeholder_text="Número da conta")
        num.pack(pady=8, padx=12)

        txt = ctk.CTkTextbox(win, width=460, height=280)
        txt.pack(padx=12, pady=8)

        def mostrar():
            try:
                n = int(num.get().strip())
            except Exception:
                txt.delete("0.0", "end")
                txt.insert("0.0", "Número de conta inválido.")
                return
            conta = self.banco.procurar_conta(n)
            if not conta:
                txt.delete("0.0", "end")
                txt.insert("0.0", "Conta não encontrada.")
                return
            txt.delete("0.0", "end")
            txt.insert("0.0", conta.exibir_extrato())

        ctk.CTkButton(win, text="Mostrar Extrato", command=mostrar).pack(pady=6)

    def _open_listar_contas(self):
        contas = self.banco.listar_contas()
        self._log("Listando contas:")
        for c in contas:
            self._log(f"Ag: {c.agencia} | Conta: {c.numero_conta} | Titular: {c.usuario.nome}")

if __name__ == "__main__":
    banco = Banco()
    app = App(banco)
    app.mainloop()
