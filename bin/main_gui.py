# main_gui.py
from interface.gui import App
from models.banco import Banco

if __name__ == "__main__":
    banco = Banco()
    app = App(banco)
    app.mainloop()
