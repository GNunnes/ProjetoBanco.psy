# models/conta.py
from models.usuario import Usuario

class ContaBancaria:
    def __init__(self, agencia: str, numero_conta: int, usuario: Usuario,
                 saldo: float = 0.0, limite: float = 500.0, numero_saques: int = 0, extrato=None):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = saldo
        self.limite = limite
        self.numero_saques = numero_saques
        self.extrato = extrato if extrato is not None else []

    def depositar(self, valor: float):
        if valor <= 0:
            return False, "Valor inválido."
        self.saldo += valor
        self.extrato.append(f"Depósito:\tR$ {valor:.2f}")
        return True, "Depósito realizado com sucesso."

    def sacar(self, valor: float, limite_saques: int = 3):
        if valor <= 0:
            return False, "Valor inválido."
        if valor > self.saldo:
            return False, "Saldo insuficiente."
        if valor > self.limite:
            return False, "Valor excede o limite de saque."
        if self.numero_saques >= limite_saques:
            return False, "Número máximo de saques excedido."
        self.saldo -= valor
        self.numero_saques += 1
        self.extrato.append(f"Saque:\t\tR$ {valor:.2f}")
        return True, "Saque realizado com sucesso."

    def exibir_extrato(self):
        if not self.extrato:
            return "Não foram realizadas movimentações."
        return "\n".join(self.extrato) + f"\n\nSaldo:\tR$ {self.saldo:.2f}"

    def to_dict(self):
        return {
            "agencia": self.agencia,
            "numero_conta": self.numero_conta,
            "usuario": self.usuario.to_dict(),
            "saldo": self.saldo,
            "limite": self.limite,
            "numero_saques": self.numero_saques,
            "extrato": self.extrato,
        }

    @classmethod
    def from_dict(cls, data):
        usuario = Usuario.from_dict(data["usuario"])
        return cls(
            agencia=data["agencia"],
            numero_conta=data["numero_conta"],
            usuario=usuario,
            saldo=data.get("saldo", 0.0),
            limite=data.get("limite", 500.0),
            numero_saques=data.get("numero_saques", 0),
            extrato=data.get("extrato", []),
        )
