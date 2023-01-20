from numbers import Number


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other
    
    def __rsub__(self, other):
        return self - other
    
    def __sub__(self, other):
        if isinstance(other, Number):
            other=Polynomial((other,))
        new = self + Polynomial(tuple([i*-1 for i in other.coefficients]))
        return new

    def __mul__(self,other):
        if isinstance(other, Number):
            other=Polynomial((other,))
        if self.degree()==0 or other.degree()==0:
            if self.degree()==0:
                return Polynomial(tuple([i*self.coefficients[0] for i in other.coefficients]))
            elif other.degree()==0:
                return Polynomial(tuple([i*other.coefficients[0] for i in self.coefficients]))
        elif self.degree()>1 and other.degree()>0:
            b=other.coefficients[0]*list(self.coefficients)
            b=tuple(b)
            b=Polynomial(b)
            for d in range (other.degree()):
                a=[i*other.coefficients[d+1] for i in self.coefficients]
                a=tuple([0]*(d+1)+a)
                a=Polynomial(a)
                b=b.__add__(a)
            return b

print(Polynomial((2,22)).__rsub__(2))