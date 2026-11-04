from app.database.schema import inicializar
from app.router.menu import Menu


def main():
    inicializar()
    menu = Menu()
    menu.ejecutar()


if __name__ == "__main__":
    main()