from Domain.film import *
from Controller.validation import *
from Repository.film import RepositoryFilm

def main():
    f = Film(2, "Arthur", "Frumos", "Actiune")
    r = RepositoryFilm()
    r.append(Film())
    r.append(f)
    s = r.where(id=1)
    print(s)

main()
