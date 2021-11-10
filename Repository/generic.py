from Controller.errors import DuplicateIdError

class Repository: # clasa pentru reposity de tipul type
    def __init__(self, type): # constructor
        self._type = type
        self._l = []

    @property
    def type(self): return self._type # getter pt tipul de reposity

    @property
    def l(self): return self._l # getter pentru lista respectiva reposity-ului

    def __len__(self): # determina numeraul de elemente
        return len(self.l)

    def __iter__(self): # face reposity-ul iterabil
        return iter(self.l)

    def __bool__(self): # verificarea daca contine elemente
        return len(self) > 0

    def __contains__(self, item): # verificare apartenenta
        if not isinstance(item, self.type): raise TypeError(
            f"Imposibil de cautat elementul de tipul {type(item)} in reposity-ul de tipul {self.type} datorita diferentelor de tip!")
        return item in self.l

    def __getitem__(self, item): # indexator de tip get
        if isinstance(item, int):
            return self.l[item]
        elif isinstance(item, self.type):
            for i in range(len(self.l)):
                if self.l[i] == item:
                    return self.l[i]

    def __setitem__(self, key, value): # indexator de tip set
        if isinstance(key, int): self.l[key] = value
        elif isinstance(key, self.type):
            for i in range(len(self.l)):
                if self.l[i] == key:
                    self.l[i] = value

    def __eq__(self, other): # operator de egalitate care nu tine cont de ordinea elementelor
        try:
            if len(self) != len(other): return False
            for elem in other:
                if not elem in self:
                    return False
            for elem in self:
                if not elem in other:
                    return False
            return True
        except: return False

    def __str__(self):
        s = ""
        for elem in self:
            s+=str(elem)+"\n"
        return s[:-1]

    def append(self, other):
        '''
        adaugarea unui element in lista
        :param other: un alt elemet de tipul tip
        :raise: TypeError, in caz ca other nu are tipul type
                DuplicateIdError, in caz ca id-ul a mai fost adaugat odata in lista
        '''
        if not isinstance(other, self.type): raise TypeError(
            f"Imposibil de adaugat elementul de tipul {type(other)} in reposity-ul de tipul {self.type} datorita diferentelor de tip!")
        #for elem in self:
        #    if elem.id == other.id:
        #        raise DuplicateIdError
        self.l.append(other)

    def extend(self, other): # adauga succesiv elementele
        try:
            for elem in other: pass
        except: raise TypeError(f"Imposibil de parcurs elementele din {other}")
        for elem in other:
            self.append(elem)

    def remove(self, other): # stergerea unui element
        if not isinstance(other, self.type): raise TypeError(
            f"Imposibil de sters elementul de tipul {type(other)} in reposity-ul de tipul {self.type} datorita diferentelor de tip!")
        self.l.remove(other)

    def clear(self): # sterge intreaga lista
        self.l.clear()

    def index(self, other, start=0, stop=-1): # gaseste index-ul unui element
        if not isinstance(other, self.type): raise TypeError(
            f"Imposibil de cautat elementul de tipul {type(other)} in reposity-ul de tipul {self.type} datorita diferentelor de tip!")
        return self.l.index(other, start, stop)

    def pop(self):  # elimina ultimul element
        return self.l.pop()

    def copy(self):  # returneaza o copie
        r = Repository(self.type)
        r._l = self.l[:]
        return r

    def sort(self, key=None, reverse=False):  # sorteaza lista
        self.l.sort(key=key, reverse=reverse)

    def where(self, **kwargs):  # cauta elemente in lista comform specificatiilor todo
        raise NotImplementedError
