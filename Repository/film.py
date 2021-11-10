from Repository.generic import Repository
from Domain.film import Film

class RepositoryFilm(Repository): # lista de filme
    def __init__(self):
        self._type = Film
        super().__init__(self._type)

    def where(self, **kwargs): # implementarea functiei de cautare
        fcts = []
        rez = self.l
        for key, value in kwargs.items():
            if key == "id":
                fcts.append(lambda argument: (argument.id == value))
                rez = list(filter(fcts[-1], rez))
            elif key == "titlu":
                fcts.append(lambda argument: (argument.titlu == value))
                rez = list(filter(fcts[-1], rez))
            elif key == "descriere":
                fcts.append(lambda argument: (argument.descriere == value))
                rez = list(filter(fcts[-1], rez))
            elif key == "gen":
                fcts.append(lambda argument: (argument.gen == value))
                rez = list(filter(fcts[-1], rez))
            elif key == "fields":
                fcts.append(lambda argument: (argument == Film.fromIterable(value)))
                rez = list(filter(fcts[-1], rez))
            elif key == "film":
                fcts.append(lambda argument: (argument == value))
                rez = list(filter(fcts[-1], rez))
            elif key == "function":
                fcts.append(value)
                rez = list(filter(fcts[-1], rez))
        # print(rez)
        r = RepositoryFilm()
        r.extend(rez)
        return r

        def call_all(element):  # apeleaza toate functiile
            for fct in fcts:
                if not fct(element):
                    return False
            return True

        rez = RepositoryFilm()
        for elem in self:
            if call_all(elem):
                rez.append(elem)
        return rez
