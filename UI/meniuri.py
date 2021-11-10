from Controller.generalservice import ServiceCRUD
from UI.menubase import *


class Meniuri:
    @staticmethod
    def CRUD(handler):  # meniu specific operatiilor CRUD
        m = Meniu()
        m.titlu = "\n\tOptiuni:\n"
        m.clear_after_input = True
        m.show_one_time = True
        m.culoaretitlu = cl.Fore.LIGHTYELLOW_EX

        o = Optiune(1, "Adauga", handler.adauga)
        o.colornume = cl.Fore.LIGHTGREEN_EX
        m.listaoptiuni.append(o)

        o = Optiune(2, "Sterge", handler.sterge)
        o.colornume = cl.Fore.LIGHTRED_EX
        m.listaoptiuni.append(o)

        o = Optiune(3, "Modifica", handler.modificare)
        o.colornume = cl.Fore.LIGHTCYAN_EX
        m.listaoptiuni.append(o)

        o = Optiune(4, "Vizualizeaza", handler.vizualizeaza)
        o.colornume = cl.Fore.LIGHTBLUE_EX
        o.clear_method = "clear after input"
        m.listaoptiuni.append(o)

        o = Optiune(5, "Cauta", handler.cauta)
        o.colornume = cl.Fore.LIGHTBLUE_EX
        o.clear_method = "clear after input"
        m.listaoptiuni.append(o)

        return m
