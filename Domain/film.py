#from Controller.validFilmClient import ValidatorFilm

class Film: # tipul de date film
    def __init__(self, id=1, titlu="Film", descriere="interesant", gen="actiune"): # constructor
        self.__id = id
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen
        #ValidatorFilm.film(self)

    def get_id(self): return self.__id                  # getter id
    def get_titlu(self): return self.__titlu            # getter titlu
    def get_descriere(self): return self.__descriere    # getter descrere
    def get_gen(self): return self.__gen                # getter gen

    def set_titlu(self, titlu):            # setter titlu
        #ValidatorFilm.titlu(titlu)
        self.__titlu = titlu

    def set_descriere(self, descriere):    # setter descriere
        #ValidatorFilm.descriere(descriere)
        self.__descriere = descriere

    def set_gen(self, gen):                # setter gen
        #ValidatorFilm.gen(gen)
        self.__gen = gen

    id = property(get_id)                               # proprietate id
    titlu = property(get_titlu, set_titlu)              # proprietate titlu
    descriere = property(get_descriere, set_descriere)  # proprietate descriere
    gen = property(get_gen, set_gen)                    # proprietate gen

    def __eq__(self, other): # operator de egalitate
        if not isinstance(other, Film): return False
        if self.id == other.id and self.descriere == other.descriere and self.gen == other.gen: return True
        return False

    def __str__(self):
        return f"Id: {self.id}\nTitlu: {self.titlu}\nDescriere: {self.descriere}\nGen: {self.gen}"

    @classmethod
    def fromStr(cls, str):
        '''
        converteste din string in Film
        :param str: sirul
        :rtype: Film
        :raise: IOException, ValueError
        '''
        try:
            sir = str.split()
            return cls(sir[0], sir[1], sir[2], sir[3])
        except: raise IOError("Film introdus incorect!")

    @classmethod
    def fromIterable(cls, it):
        '''
        converteste primele date dintr-un iterabil la Film
        :param it: list/tuple/...
        :rtype: Film
        :raise: ValueError
        '''
        return cls(it[0], it[1], it[2], it[3])