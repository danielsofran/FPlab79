from Repository.generic import Repository
from Domain.client import Client

class RepositoryClient(Repository): # lista de clienti
    def __init__(self):
        self._type = Client
        super().__init__(self._type)

    def where(self, **kwargs): # implementarea functiei de cautare
        fcts = []
        for key, value in kwargs.items():
            if key=="id": fcts.append(lambda elem: elem.id == value)
            elif key=="nume": fcts.append(lambda elem: elem.nume == value)
            elif key=="cnp": fcts.append(lambda elem: elem.cnp == str(value))
            elif key=="fields": fcts.append(lambda elem: elem == Client.fromIterable(value))
            elif key=="client": fcts.append(lambda elem: elem == value)
            elif key=="function": fcts.append(value)
        def call_all(elem):
            for fct in fcts:
                if not fct(elem):
                    return False
            return True
        rez = RepositoryClient()
        for elem in self:
            if call_all(elem):
                rez.append(elem)
        return rez


