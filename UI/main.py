from UI.meniuri import *
from UI.handle import Handler
from Controller.service import ServiceFilme, ServiceClienti


def gestioneaza(service):  # submeniul 1
    h = Handler(service)
    meniu = Meniuri.CRUD(h)
    meniu.run()


def run():  # meniul principal
    m = Meniu("\n\tMENIU\n", clear_after_input=True)
    m.culoaretitlu = cl.Fore.LIGHTMAGENTA_EX
    sfilme = ServiceFilme()
    sclienti = ServiceClienti()
    o = Optiune(1, "Gestioneaza lista de filme", gestioneaza, sfilme)
    m += o
    o = Optiune(2, "Gestioneaza lista de clienti", gestioneaza, sclienti)
    m += o
    m.run()
