# main_cli.py
from models.banco import Banco

def teste_rapido():
    banco = Banco()
    ok, msg = banco.criar_usuario("Gustavo", "01-01-1982", "12345678901", "Rua X, 100 - Bairro - Cidade/UF")
    print("Criar usuário:", ok, msg)
    conta, msg = banco.criar_conta("12345678901")
    print("Criar conta:", conta.numero_conta if conta else None, msg)
    ok, msg = banco.depositar(conta.numero_conta, 200.0)
    print("Depositar:", ok, msg)
    ok, msg = banco.sacar(conta.numero_conta, 50.0)
    print("Sacar:", ok, msg)
    print("Extrato:\n", conta.exibir_extrato())

if __name__ == "__main__":
    teste_rapido()
