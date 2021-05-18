a = 1
b = 2
print(a + b)
#
a = 'fr'
b = 'og'
print(a + b)
#
a = 1
b = 2.5
print(a + b)
#
type(1)
type(abs)
type(int)
#
class Polynomial:
    def __init__(self, coefs):
        self.coefficients = coefs
    def degree(self):
        return len(self.coefficients) - 1
    def __str__(self):
        coefs = self.coefficients
        terms = []
        # Degree 0 and 1 terms conventionally habe different representation.
        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() > 0 and coefs[1]:
            terms.append(f"{coefs[1]}x")
        # Remaining terms look like cx^d, though factors of a are dropped.
        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start = 2) if c]
        # Sum polynomial terms from high to low exponent.
        return " + ".join(reversed(terms)) or "0"
    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"
f = Polynomial((0, 1, 2))
f = Polynomial((1, 2, 0, 1, 5))
f.coefficients
f.degree()
print(f)
#
2 == 2.0
2.0 == 2 + 0j
(0, 1, "f") == (0, 1 + 0j, 'f')
(0, 1, "f") == (0., 1 + 0j, 'g')
(0, 1, "f") == (0., 1 + 0j)
# 
from example_code.polynomial import Polynomial # import unsuccessful
a = Polynomial((1, 0, 1))
b = Polynomial((1, 0, 1))
a == b 
#
id(a)
id(b)

