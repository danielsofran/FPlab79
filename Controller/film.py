from Domain.film import Film
from Controller.validation import ValidatorFilm
from Repository.film import RepositoryFilm

class ServiceFilme:
    def __init__(self): # constructor
        self.__repo = RepositoryFilm()
        self.__msg = ""

    @property
    def repo(self): return self.__repo # getter la repository
    @repo.setter
    def repo(self, val): self.__repo = val # setter la repository

    @property
    def msg(self): return self.__msg # getter pt mesajul rezultat
    @msg.setter
    def msg(self, txt): self.__msg = txt # setter pt mesajul rezultat

    def adauga(self, other): # adauga un iterabil in repository
        try: ValidatorFilm.iterable(other)
        except Exception as ex: self.msg = ex.args[0]
        else:
            obj = Film.fromIterable(other)
            for elem in self.repo:
                if elem.id == obj.id:
                  self.msg = f"Id {obj.id} duplicat in lista de filme!"
            else: self.repo.append(obj)

    def sterge(self, other): # sterge un iterabil din repository
        try: ValidatorFilm.iterable(other)
        except Exception as ex: self.msg = ex.args[0]
        else:
            obj = Film.fromIterable(other)
            if not obj in self.repo:
                self.msg = f"Imposibil de sters filmul {obj.titlu} din lista din cauza faptului ca nu a fost adaugat!"
            else:
                self.repo.remove(obj)

    def modificare(self, initial, final): # inlocuieste iterabilul initial cu cel final
        try: ValidatorFilm.iterable(initial)
        except Exception as ex: self.msg = ex.args[0]
        else:
            try: ValidatorFilm.iterable(final)
            except Exception as ex: self.msg = ex.args[0]
            else:
                o1 = Film.fromIterable(initial)
                o2 = Film.fromIterable(final)
                if not o1 in self.repo: self.msg = f"Imposibil de actualizat filmul {o1.titlu} din lista din cauza faptului ca nu a fost adaugat!"
                else: self.repo[o1] = o2 #########################################################################################################

    def vizualizare(self): # afiseaza toate filmele din repository
        if len(self.repo) == 0:
            self.msg = "Nu exista filme in lista!"
        else: self.msg = "Lista de Filme:\n" + str(self.repo)

    def cautare(self, **kwargs): # cauta dupa niste criterii in repository
        if len(kwargs) == 0:
            self.msg = "Nu ati introdus criterii de cautare!"
        else:
            rez = self.repo.where(**kwargs)
            if len(rez) == 0: self.msg = "Nu exista filme care sa respecte criteriile date!"
            else: self.msg = "Rezultate:\n"+str(rez)
