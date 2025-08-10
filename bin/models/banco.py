# models/banco.py
import json
import os
from models.usuario import Usuario
from models.conta import ContaBancaria
from typing import Optional

class Banco:
    def __init__(self, agencia: str = "0001", data_folder: str = "data"):
        self.agencia = agencia
        self.data_folder = data_folder
        os.makedirs(self.data_folder, exist_ok=True)
        self.usuarios_file = os.path.join(self.data_folder, "usuarios.json")
        self.contas_file = os.path.join(self.data_folder, "contas.json")
        self.usuarios: list[Usuario] = []
        self.contas: list[ContaBancaria] = []
        self.load()

    # ---------- Usuários ----------
    def filtrar_usuario(self, cpf: str) -> Optional[Usuario]:
        for u in self.usuarios:
            if u.cpf == cpf:
                return u
        return None

    def criar_usuario(self, nome: str, data_nascimento: str, cpf: str, endereco: str):
        if self.filtrar_usuario(cpf):
            return False, "Já existe usuário com esse CPF."
        usuario = Usuario(nome, data_nascimento, cpf, endereco)
        self.usuarios.append(usuario)
        self.save()
        return True, "Usuário criado com sucesso."

    # ---------- Contas ----------
    def criar_conta(self, cpf: str):
        usuario = self.filtrar_usuario(cpf)
        if not usuario:
            return None, "Usuário não encontrado."
        numero_conta = len(self.contas) + 1
        conta = ContaBancaria(self.agencia, numero_conta, usuario)
        self.contas.append(conta)
        self.save()
        return conta, "Conta criada com sucesso."

    def procurar_conta(self, numero_conta: int) -> Optional[ContaBancaria]:
        for c in self.contas:
            if c.numero_conta == numero_conta:
                return c
        return None

    def listar_contas(self):
        return self.contas

    # ---------- Operações que atualizam e salvam ----------
    def depositar(self, numero_conta: int, valor: float):
        conta = self.procurar_conta(numero_conta)
        if not conta:
            return False, "Conta não encontrada."
        ok, msg = conta.depositar(valor)
        if ok:
            self.save()
        return ok, msg

    def sacar(self, numero_conta: int, valor: float, limite_saques: int = 3):
        conta = self.procurar_conta(numero_conta)
        if not conta:
            return False, "Conta não encontrada."
        ok, msg = conta.sacar(valor, limite_saques=limite_saques)
        if ok:
            self.save()
        return ok, msg

    # ---------- Persistência ----------
    def save(self):
        with open(self.usuarios_file, "w", encoding="utf-8") as f:
            json.dump([u.to_dict() for u in self.usuarios], f, indent=4, ensure_ascii=False)
        with open(self.contas_file, "w", encoding="utf-8") as f:
            json.dump([c.to_dict() for c in self.contas], f, indent=4, ensure_ascii=False)

    def load(self):
        # carregar usuários
        if os.path.exists(self.usuarios_file):
            with open(self.usuarios_file, "r", encoding="utf-8") as f:
                usuarios_data = json.load(f)
                self.usuarios = [Usuario.from_dict(u) for u in usuarios_data]
        # carregar contas
        if os.path.exists(self.contas_file):
            with open(self.contas_file, "r", encoding="utf-8") as f:
                contas_data = json.load(f)
                self.contas = [ContaBancaria.from_dict(c) for c in contas_data]
