# %%
class Polynomial:
    def __init__(self, terms=None):
        self.poly = {}  # creating a empty dictionary
        if terms:
            for coeff, exp in terms:
                self.poly[exp] = self.poly.get(exp,
                                               0) + coeff  # using exponenets as keys and coeffecient as value. also creates a single key for each exponent
            self.poly = {e: c for e, c in self.poly.items() if c != 0}  # removes exponents where coefficient is 0
        else:
            self.poly = {}  # empty dictionary if no terms are given

    def iszero(self):
        return len(self.poly) == 0  # returns true if empty dictionary, i.e. zero polynomial

    def __add__(self, other):  # creating method to add polynomial
        result = self.poly.copy()
        for exp, coeff in other.poly.items():
            result[exp] = result.get(exp,
                                     0) + coeff  # adding coefficients wherever other ploynomial has same exponent as self
        return Polynomial(
            [(c, e) for e, c in result.items()])  # result is in form (e,c), reversing order so we can clean the result

    def __sub__(self, other):
        result = self.poly.copy()
        for exp, coeff in other.poly.items():
            result[exp] = result.get(exp,
                                     0) - coeff  # substracting coefficients wherever other ploynomial has same exponent as self
        return Polynomial(
            [(c, e) for e, c in result.items()])  # result is in form (e,c), reversing order so we can clean the result

    def __mul__(self, other):
        result = {}
        for e1, c1 in self.poly.items():
            for e2, c2 in other.poly.items():  # iterating over each element of other for each element of self
                exp = e1 + e2  # adding the power of exponents when multiplying
                result[exp] = result.get(exp,
                                         0) + c1 * c2  # multiplying the coefficients and assigning them to the relevant exponent
        return Polynomial(
            [(c, e) for e, c in result.items()])  # result is in form (e,c), reversing order so we can clean the result

    def sortPoly(self):
        return sorted(self.poly.items(), key=lambda i: i[0], reverse=True)  # sorting tuples by exponent

    def __eq__(self, other):
        p1 = self.sortPoly()
        p2 = other.sortPoly()
        if len(p1) != len(p2):
            return False  # if length is unequal then polynomials will be unequal
        else:
            for (e1, c1), (e2, c2) in zip(p1, p2):
                if e1 != e2:  # comparing exponent first
                    return False
                elif c1 != c2:  # comparing coefficients if exponents are equal
                    return False
            return True

    def __ne__(self, other):
        return not self.__eq__(other)  # return opposite of equal to function

    def __lt__(self, other):
        p1 = self.sortPoly()
        p2 = other.sortPoly()
        for (e1, c1), (e2, c2) in zip(p1, p2):  # Compare term by term (exponent, then coefficient)
            if e1 < e2:
                return True
            elif e1 > e2:
                return False
            else:  # exponents equal, compare coefficients
                if c1 < c2:
                    return True
                elif c1 > c2:
                    return False
        return len(p1) < len(p2)  # If all compared terms are equal, shorter polynomial is smaller

    def __le__(self, other):
        p1 = self.sortPoly()
        p2 = other.sortPoly()
        for (e1, c1), (e2, c2) in zip(p1, p2):  # Compare term by term (exponent, then coefficient)
            if e1 < e2:
                return True
            elif e1 > e2:
                return False
            else:  # exponents equal, compare coefficients
                if c1 < c2:
                    return True
                elif c1 > c2:
                    return False
        return len(p1) <= len(
            p2)  # If all compared terms are equal, shorter polynomial is smaller, or equal if same length

    def __gt__(self, other):
        return not self.__le__(other)  # return opposite of less than equal to function

    def __ge__(self, other):
        return not self.__lt__(other)  # return opposite of less than function

    def __str__(self):
        if self.iszero():
            return "0"  # return 0 if zero polynomial
        terms = []
        for exp, coeff in self.sortPoly():
            if exp == 0:
                terms.append(f"{coeff}")  # print only coefficient if exponent is 0
            elif exp == 1:  # print x if exponent is 1
                if coeff != 1:  # print coefficient only if it is not equal to 1
                    terms.append(f"{coeff}x")
                else:
                    terms.append("x")  # print x if exponent is 1 and coefficint is 1
            else:  # print power if exponent is greater than 1
                if coeff != 1:  # print coefficient only if it is not equal to 1
                    terms.append(f"{coeff}x^{exp}")
                else:
                    terms.append(f"x^{exp}")
        expr = terms[0]  # first term with highest exponent
        for t in terms[1:]:
            if t.startswith('-'):  # if coefficient has -
                expr += " - " + t[1:]  # adding minus and printing the string without the minus sign
            else:
                expr += " + " + t  # adding plus sign and printing the string
        return expr


# %%
p = Polynomial([(3, 4), (-17, 2), (-3, 1), (5, 0)])
q = Polynomial([(1, 1), (1, 0)])
print("p =", p)
print("q =", q)

print("is p a zero polynomial?", p.iszero())
print("is p a zero polynomial?", q.iszero())

print("p + q =", p + q)
print("p - q =", p - q)
print("p * q =", p * q)
print("p == q?", p == q)
print("p <= q?", p <= q)
print("p < q?", p < q)
print("p >= q?", p >= q)
print("p > q?", p > q)
print("p != q?", p != q)
# %%
p = Polynomial([(2, 1), (1, 2)])
q = Polynomial([(2, 1), (1, 2)])
print("p =", p)
print("q =", q)

print("is p a zero polynomial?", p.iszero())
print("is q a zero polynomial?", q.iszero())

print("p + q =", p + q)
print("p - q =", p - q)
print("p * q =", p * q)
print("p == q?", p == q)
print("p <= q?", p <= q)
print("p < q?", p < q)
print("p >= q?", p >= q)
print("p > q?", p > q)
print("p != q?", p != q)

print("is p-q a zero polynomial?", (p - q).iszero())

# %%
p = Polynomial([(0, 0), (0, 3)])
print("p =", p)
print("is p a zero polynomial?", p.iszero())
# %%
p = Polynomial([(1, 3), (2, 5), (2, 3)])
q = Polynomial([(-3, 3), (3, 4)])

print("p =", p)
print("q =", q)

print("is p a zero polynomial?", p.iszero())
print("is q a zero polynomial?", q.iszero())

print("p + q =", p + q)
print("p - q =", p - q)
print("p * q =", p * q)
print("p == q?", p == q)
print("p <= q?", p <= q)
print("p < q?", p < q)
print("p >= q?", p >= q)
print("p > q?", p > q)
print("p != q?", p != q)
