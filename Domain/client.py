#from Controller.validFilmClient import ValidatorClient

class Client: # tipul de date client
    def __init__(self, id=1, nume="Șofran Daniel", cnp="1632084562102"):
        self.__id = id
        self.__nume = nume
        self.__cnp = cnp
        #ValidatorClient.client(self)
        #self.__cnp = str(cnp)

    def get_id(self): return self.__id      # getter id
    def get_nume(self): return self.__nume  # getter nume
    def get_cnp(self): return self.__cnp    # getter cnp

    def set_nume(self, nume):       # setter nume
        #ValidatorClient.nume(nume)
        self.__nume = nume

    def set_cnp(self, cnp):
        #ValidatorClient.cnp(cnp)    # setter cnp
        self.__cnp = str(cnp)

    id = property(get_id)               # proprietate id
    nume = property(get_nume, set_nume) # proprietate nume
    cnp = property(get_cnp, set_cnp)    # proprietate cnp

    def __eq__(self, other): # operator de egalitate
        if not isinstance(other, Client): return False
        if self.id == other.id and self.nume == other.nume and self.cnp == other.cnp: return True
        return False

    def __str__(self): # conversia la string
        return f"Id: {self.id}\nNume: {self.nume}\nCNP: {self.cnp}"

    @classmethod
    def fromStr(cls, str):
        '''
        converteste din string in Client
        :param str: sirul
        :rtype: Client
        :raise: IOException, ValueError
        '''
        try:
            sir = str.split()
            return cls(sir[0], sir[1], sir[2])
        except:
            raise IOError("Client introdus incorect!")

    @classmethod
    def fromIterable(cls, it):
        '''
        converteste primele date dintr-un iterabil la Client
        :param it: list/tuple/...
        :rtype: Client
        :raise: ValueError
        '''
        return cls(it[0], it[1], it[2])