from __future__ import division
class Complex :

    def __init__(self, Re, Im):
        self.__Re = Re
        self.__Im = Im

    def __add__(self,New):
        return(Complex(self.__Re + New.__Re, self.__Im + New.__Im))

    def __sub__(self,New):
        return(Complex(self.__Re - New.__Re, self.__Im - New.__Im))

    def __mul__(self,New):
        return(Complex(self.__Re * New.__Re, self.__Im * New.__Im))

    def __truediv__(self,New):
        return(Complex(self.__Re / New.__Re, self.__Im / New.__Im))

    def __abs__(self,New):
        return(Complex(abs(self.__Re + New.__Re),abs( self.__Im + New.__Im)))

    def __eq__(self,New):
        return(Complex(self.__Re == New.__Re, self.__Im == New.__Im))

    def __ne__(self,New):
        return(Complex(self.__Re != New.__Re, self.__Im != New.__Im))


if __name__ == "__main__":
    c1 = Complex(13,11)
    c2 = Complex(12,13)
    c3 = c1 + c2
    c4 = c1 != c2
    c5 = c2 == c3
    c6 = c2 / c3
    c7 = c2*c3
    print(c3)
    print(c4)
    print(c5)
    print(c6)
    print(c7)


