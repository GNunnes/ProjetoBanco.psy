<h1 align="center">🏦 Projeto Banco - Interface Gráfica em Python</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/CustomTkinter-UI%20Framework-blueviolet?style=for-the-badge" alt="CustomTkinter Badge"/>
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange?style=for-the-badge" alt="Status Badge"/>
</p>

---

## 📌 Sobre o projeto
Este é um **Sistema Bancário** desenvolvido em **Python 3.13** com interface gráfica construída utilizando **CustomTkinter**.

A aplicação simula operações bancárias como:
- Cadastro de usuários
- Criação de contas
- Depósitos
- Saques
- Consulta de extratos
- Listagem de contas

Com um design moderno, organizado e responsivo, este projeto é perfeito para estudos de **Python OOP**, **Tkinter/CustomTkinter** e boas práticas de estrutura de código.

---

## 🖼️ Screenshot

![Screenshot do Sistema](./img/TelaInicial.png)

> Interface amigável e totalmente funcional.

---

![Screenshot do Sistema](./img/Menu01.png)

> Janela Extrato.

---

![Screenshot do Sistema](./img/Menu02.png)

> Janela Sacar.

---

![Screenshot do Sistema](./img/Menu03.png)

> Janela Depósito.

---

![Screenshot do Sistema](./img/Menu04.png)

> Janela Criar Conta.

---

![Screenshot do Sistema](./img/Menu05.png)

> Janela Criar Usuário.

## 🚀 Tecnologias utilizadas

- **Python 3.13**
- **CustomTkinter**
- **Programação Orientada a Objetos (POO)**

---

## 📂 Estrutura do Projeto

```
projeto_banco.psy/
│
├── src/
│ ├── interface/
│ │ └── gui.py      # Interface gráfica
│ ├── models/
│ │ ├── banco.py    # Lógica de negócio do banco
│ │ ├── conta.py    # Classe de conta
│ │ └── usuario.py  # Classe de usuário
│ ├── main_cli.py   # Interface de linha de comando
│ ├── main_gui.py   # Inicia a aplicação gráfica
│ └── teste_gui.py  # Teste rápido da GUI
│
├── README.md
└── requirements.txt
```

---

## ⚙️ Como executar

***1️⃣ Clone o repositório***

```bash
git clone https://github.com/seu-usuario/projeto_banco.psy.git
cd projeto_banco.psy
```
***2️⃣ Crie e ative o ambiente virtual***
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
***3️⃣ Instale as dependências***
```
pip install -r requirements.txt
```
***4️⃣ Execute a aplicação gráfica***
```
python -m src.main_gui
```
## 👤 Desenvolvido por
- [LinkedIn](https://www.linkedin.com/in/gustavo-nunnes) *(gustavo-nunnes)*
- Email: **gustavonunnes@hotmail.com**
- GitHub: [@GNunnes](https://github.com/GNunnes)