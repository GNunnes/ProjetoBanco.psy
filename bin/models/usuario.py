# models/usuario.py
class Usuario:
    def __init__(self, nome: str, data_nascimento: str, cpf: str, endereco: str):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

    def to_dict(self):
        return {
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "cpf": self.cpf,
            "endereco": self.endereco,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            nome=data["nome"],
            data_nascimento=data["data_nascimento"],
            cpf=data["cpf"],
            endereco=data["endereco"],
        )
