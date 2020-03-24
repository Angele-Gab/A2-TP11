class Cercle :

    def __init__(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, c):
        self.__radius=c

    def __add__(self,c1):
        return(Cercle(self.__radius + c1.__radius))

    def __lt__(self,c1):
        return(self.__radius < c1.__radius)

    def __gt__(self,c1) :
        return (self.__radius > c1.__radius)


if __name__ == "__main__":
    c1 = Cercle(2)
    c2 = Cercle(3)
    c3 = c1 + c2
    c4 = c1 < c2
    c5 = c2 > c3
    print(c3)
    print(c4)
    print(c5)
