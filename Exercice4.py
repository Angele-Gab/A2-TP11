class Duree :

    def __init__(self,heure, minute, seconde):
        self.__h = heure
        self.__m = minute
        self.__s = seconde

    def Affichage(self):
        print(self.__h,"h", self.__m,"min",self.__s,"sec")

    def __add__(self,New):
        Heure = 0
        Minute = 0
        Seconde = self.__s + New.__s
        while Seconde >= 60 :
            Seconde -= 60
            Minute += 1
        Minute += (self.__m + New.__m)
        while Minute >= 60 :
            Minute -= 60
            Heure += 1
        Heure += (self.__h + New.__h)
        print(Heure,"h", Minute,"min",Seconde,"sec")


if __name__ == "__main__":
    T1 = Duree(13,11,56)
    T2 = Duree(12,58,49)
    T3 = T1 + T2

    T1.Affichage()

