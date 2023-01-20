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
        return other+(self*-1)
    
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
        elif self.degree()>0 and other.degree()>0:
            
            b=[i*other.coefficients[0] for i in self.coefficients]
            
            b=tuple(b)
            b=Polynomial(b)
            for d in range (other.degree()):
                
                a=[i*other.coefficients[d+1] for i in self.coefficients]
                
                a=tuple([0]*(d+1)+a)
                
                a=Polynomial(a)
                b=b+a
                
            return b
    def __rmul__(self,other):
        if isinstance(other, Number):
            other=Polynomial((other,))
        if self.degree()==0 or other.degree()==0:
            if other.degree()==0:
                return Polynomial(tuple([(i)*(self.coefficients[0]+1) for i in self.coefficients]))
            elif self.degree()==0:
                return Polynomial(tuple([i*other.coefficients[0] for i in other.coefficients]))
        elif self.degree()>0 and other.degree()>0:
            b=[i*other.coefficients[0] for i in self.coefficients]
            b=tuple(b)
            b=Polynomial(b)
            for d in range (other.degree()):
                a=[i*other.coefficients[d+1] for i in self.coefficients]
                a=tuple([0]*(d+1)+a)
                a=Polynomial(a)
                b=b.__add__(a)
            return b
    def __pow__(self,other):
        result=self
        for i in range (other-1):
            result=self*result
        return result
    def __call__(self,other):
        powered=[self.coefficients[i]*other**i for i in range(len(self.coefficients))]
        powa=sum(powered)
        return powa
    def dx(self):
        if self.degree()==0:
            return Polynomial((0,))
        listr=[[list(self.coefficients)[i]*i for i in range(len(self.coefficients))][i+1] for i in range(len(list(self.coefficients))-1)]
        listr=Polynomial(tuple(listr))
        return listr
    
    
    
def derivative(thang):
        return thang.dx()
