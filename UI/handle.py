from Controller.service import *


class Input:
    @staticmethod
    def film():
        id = input("Id: ")
        titlu = input("Titlu: ")
        descriere = input("Descriere: ")
        gen = input("Gen: ")
        return (id, titlu, descriere, gen)

    @staticmethod
    def client():
        id = input("Id: ")
        nume = input("Nume: ")
        cnp = input("CNP: ")
        return (id, nume, cnp)


class Handler:
    def __init__(self, service):
        if isinstance(service, ServiceFilme):
            self.__type = Film
        elif isinstance(service, ServiceClienti):
            self.__type = Client
        self.__service = service

    @property
    def type(self):
        return self.__type

    @property
    def service(self):
        return self.__service

    @property
    def singular(self):
        if self.type == Film:
            return "film"
        elif self.type == Client:
            return "client"

    def input(self):
        if self.type == Film:
            return Input.film()
        elif self.type == Client:
            return Input.client()

    def adauga(self):
        print(f"Introduceti un {self.singular}:\n")
        t = self.input()
        self.service.adauga(t)
        print(self.service)

    def sterge(self):
        print(f"Introduceti specificatiile dorite:\n")
        t = self.input()
        self.service.sterge(t)
        print(self.service)

    def modificare(self):
        print(f"Introduceti {self.singular}ul care urmeaza sa fie inlocuit:\n")
        t1 = self.input()
        print(f"Introduceti {self.singular}ul nou:\n")
        t2 = self.input()
        self.service.modificare(t1, t2)
        print(self.service)

    def vizualizeaza(self):
        self.service.vizualizare()
        print(self.service)

    def cauta(self):
        print(f"Introduceti optiunile de cautare:\n")
        t = self.input()
        self.service.cautare(t)
        print(self.service)
