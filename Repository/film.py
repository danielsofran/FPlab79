from Repository.generic import Repository
from Domain.film import Film

class RepositoryFilm(Repository): # lista de filme
    def __init__(self):
        self._type = Film
        super().__init__(self._type)

    def where(self, **kwargs): # implementarea functiei de cautare
        fcts = []
        for key, value in kwargs.items():
            if key=="id": fcts.append(lambda elem: elem.id == value)
            elif key=="titlu": fcts.append(lambda elem: elem.titlu == value)
            elif key=="descriere": fcts.append(lambda elem: elem.descriere == value)
            elif key=="gen": fcts.append(lambda elem: elem.gen == value)
            elif key=="fields": fcts.append(lambda elem: elem == Film.fromIterable(value))
            elif key=="film": fcts.append(lambda elem: elem == value)
            elif key=="function": fcts.append(value)
        def call_all(elem):
            for fct in fcts:
                if not fct(elem):
                    return False
            return True
        rez = RepositoryFilm()
        for elem in self:
            if call_all(elem):
                rez.append(elem)
        return rez


