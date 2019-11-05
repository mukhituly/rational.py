from matrix import *
from vector import *
from rational import *

def gcd( n1, n2 ) :
    if n1 == 0 and n2 == 0 :
        raise ArithmeticError( "Invalid input" )
    while n2:
        temp = n1
        n1 = n2
        n2 = temp % n2
    return n1

class Rational( Number ) :
    # This means that Rational inherits from Number.
    def __init__( self, num, denom = 1 ) :
        if denom == 0:
            raise ValueError("Denom can't be zero!")
        self.num = num
        self.denom = denom
        self.normalize()

    def normalize(self):
        if gcd(self.num, self.denom) != 1:
            gcd_common = gcd(self.num, self.denom)
            self.num = self.num // gcd_common
            self.denom = self.denom // gcd_common
        return self 
        
    def __repr__(self):
        string = ''
        string += (str(int(self.num)))
        if self.denom != 1:
                string += (' / ')
                string += (str(int(self.denom)) )
        return string

    def __neg__(self):
        return Rational( -self.num, self.denom)

    def __add__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)
        return Rational( (self.num * other.denom) + (other.num * self.denom), self.denom * other.denom)

    def __sub__( self, other ) : 
        if not isinstance(other, Rational):
            other = Rational(other)
        return Rational( (self.num * other.denom) - (other.num * self.denom), self.denom * other.denom)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)
        return Rational( (self.num * other.num) , (self.denom * other.denom) )

    def __truediv__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)
        return Rational( (self.num * other.denom) , (self.denom * other.num) )

    def __rmul__( self, other ) :
        return self.__mul__(other)

    def __rtruediv__( self, other ):
        return self.__truediv__(other)

    def __eq__( self, other ):
        if not isinstance(other, Rational):
            other = Rational(other)
        return self.num == other.num and self.denom == other.denom

    def __ne__( self, other ):
        if not isinstance(other, Rational):
            other = Rational(other)
        return self.num != other.num or self.denom != other.denom

    def __lt__( self, other ):
        if not isinstance(other, Rational):
            other = Rational(other)
        return self.num * other.denom < self.denom * other.num

    def __gt__( self, other ):
        if not isinstance(other, Rational):
            other = Rational(other)
        return self.num * other.denom > self.denom * other.num

    def __le__( self, other ):
        if not isinstance(other, Rational):
            other = Rational(other)
        return self.num * other.denom <= self.denom * other.num

    def __ge__( self, other ):
        if not isinstance(other, Rational):
            other = Rational(other)
        return self.num * other.denom >= self.denom * other.num