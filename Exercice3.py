class Rational :

    def __init__(self, numerator , denominator ):
        self.__num = numerator
        self.__den = denominator

    def __add__(self,New):
        Num1 = self.__num * New.__den
        Num2 = New.__num * self.__den
        Den = self.__den * New.__den
        return(Rational(Num1 + Num2, Den))

    def __sub__(self,New):
        Num1 = self.__num * New.__den
        Num2 = New.__num * self.__den
        Den = self.__den * New.__den
        return(Rational(Num1 - Num2, Den))

    def __mul__(self,New):
        return Rational(self.__num * New.__num , self.__den * New.__den)

    def __truediv__(self,New):
        Num = self.__num * New.__den
        Den = self.__den * New.__num
        return(Rational(Num , Den))

    def __eq__(self,New):
        return(self.__num == New.__num and self.__den == New.__den)


if __name__ == "__main__":
    R1 = Rational(13,11)
    R2 = Rational(12,13)
    R3 = R1 + R2
    print(R3)
    R4 = R1 - R2
    print(R4)
    R5 = R1 * R2
    print(R5)
    R6 = R1 / R2
    print(R6)
    print(R1 == R2)

