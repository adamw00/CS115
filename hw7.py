# *********************************************
# Name     : Adam Woo
# Pledge   : I pledge my honor that I have abided by the Stevens Honor System.
# Favorite flavor of dorito : I'm alergic, but I guess cool ranch.
# *********************************************

class Term:
    # A class storing two numbers to represent a monomial k*x^n
    
    def __init__(self, coef=1, exp=0): #myTerm = Term(...)
        ''' Term(coef, exp) creates a new term. If no coef or exp are provided, they default to 0. '''
        self.coef = coef # k
        self.exp = exp   # n
        
    def __str__(self): # print(myTerm)
        ''' Returns a string representation of the term '''
        return str(self.coef) + "x^" + str(self.exp)

    # TODO
    def __eq__(self, other): # myTerm == other
        ''' Returns a boolean if two terms are equal to each other '''
        return self.coef == other.coef and self.exp == other.exp

    # TODO
    def __call__(self, input): # myTerm(input)
        ''' Given x=input, return the evaluation of the term at that x'''
        return self.coef * (input**self.exp)

    # TODO
    def __neg__(self): # otherTerm = -myTerm
        '''returns a new term, with the coef negated with respect to self'''
        x = Term(self.coef, self.exp)
        x.coef = x.coef*-1
        return x
    
# LinkedPolynomial
# Adapted in java by Antonio Nicolosi from  
# https://introcs.cs.princeton.edu/java/92symbolic/LinkedPolynomial.java, (c) 2000-2018
# Adapted to Python by Justin Barish, 2018
# Refactored by Toby Dalton, 2019 and Dom DiMaggio, 2020


class LinkedPolynomial:
# This class represents a polynomial, by a list of Terms
# It is assumed that every input polynomial will be in
# Correct form - that is, no 0 coefficients and the
# exponent is strictly decreasing
    
    def  __init__(self, polyList=[]): # myPoly = LinkedPolynomial(...)
        ''' Creates a new LP object '''
        self.polyList = polyList.copy()

    def addTerm(self, t): # myPoly.addterm(Term(coef, exp))
        ''' Adds a given term to the LP - assume it is valid '''
        self.polyList.append(t)

    def createListFromNumbers(self,numList): # myPoly2; myPoly2.createListFromNumber(...)
        ''' Creates a polynomial given a list of tuples
        Assumes the list to be in the form [(coef1, exp1), (coef2, exp2)...]
        with no duplicate exponents, and exponents in descending order
        and no 0 exponents. '''
        for i in range(len(numList)):
            t = Term(numList[i][0], numList[i][1])
            self.polyList.append(t)
            
    def __len__(self): # len(myPoly)
        ''' Returns the length of the polynomial (number of nonzero monomials)'''
        return len(self.polyList)
    
    def __str__(self): # print(myPoly)
        ''' Returns a string representation of the polynomial '''
        if len(self) == 0: return ""
        ans = str(self.polyList[0].coef) + "x^" + str(self.polyList[0].exp)
        for i in range(1, len(self)):
            coef = self.polyList[i].coef
            exp = self.polyList[i].exp
            if coef > 0:
                ans += " + " + str(coef) + "x^" + str(exp)
            elif coef < 0:
                ans += " - " + str(-coef) + "x^" + str(exp) 
        return ans    
    
    def __add__(self, otherPoly): # addPoly = myPoly + otherPoly
        ''' Returns a polynomial representing the sum of self and otherPoly 
        Note: If both inputs are properly ordered, so will the outcome be! '''
        result = LinkedPolynomial() # Our sum polynomial
        i = 0 # Tracks where in self we are
        j = 0 # Tracks where in otherPoly we are
        
        # Essentially do a merge(sort) style combination of the two
        while i < len(self) or j <len(otherPoly) : # Continue until both the two are exhausted

            if i < len(self): # If not at end of self? make x that
                x = self.polyList[i]
            else: # Else self is exhausted,  add from other
                y = otherPoly.polyList[j]
                result.addTerm(Term(y.coef, y.exp))
                j += 1
                continue

            if j < len(otherPoly): # Now, if not at end of other? make y that
                y = otherPoly.polyList[j]
            else: # Else other is exhausted, add from self
                result.addTerm(Term(x.coef, x.exp))
                i += 1
                continue

            if x.exp == y.exp: # If the two exp are the same, combine them into sum
                coef = x.coef + y.coef
                if (coef != 0): # Only add if not 0 !
                    result.addTerm(Term(coef, x.exp))
                i += 1
                j += 1
            elif x.exp < y.exp: # Add the larger exp otherwise.
                result.addTerm(Term(y.coef, y.exp))
                j += 1
            else:
                result.addTerm(Term(x.coef, x.exp))
                i += 1

        return result
  
    # TODO
    def __eq__(self, other): # myPoly == other
        '''Checks if 2 polynomials are equal. Note no polynomials will have 0-coefficient terms.
        Hint: If two LP are equal, then they will be identical in every way '''
        goal = len(self.polyList)
        count = 0
        for x in range(len(self.polyList)):
            if self.polyList[x] == other.polyList[x]:
                count += 1
        return count == goal

    # TODO
    def __call__(self, input): # myPoly(input)
        ''' Evaluates self at x=input - should use Term's __call__ '''
        total = 0
        for x in range(len(self.polyList)):
            total += self.polyList[x](input)
        return total

    # TODO
    def __neg__(self): # negPoly = -myPoly
        ''' Return an LP representing -1 * self - should use Term's __neg__
        do NOT modify self  while doing this '''
        l = self.polyList.copy()
        pp = LinkedPolynomial(l)
        for x in range(len(pp.polyList)):
            pp.polyList[x] = pp.polyList[x].__neg__()
        return pp
        

    # TODO
    def __sub__(self, other): # subPoly = myPoly - other
        ''' Returns a new LP representing self - other - should use __add__ !
        do NOT modify self or other while doing this '''
        l = other.polyList.copy()
        poopy = LinkedPolynomial(l)
        poopy = poopy.__neg__()
        return self.__add__(poopy)

    # TODO
    def __mul__(self, otherPoly): # mulPoly = myPoly * otherPoly
        '''multiply 2 polynomials together
        must return a new polynomial without changing
        self & otherPoly, and be ordered correctly
        Hint: do it on paper first! '''
        ls = self.polyList.copy()
        lo = otherPoly.polyList.copy()
        self1 = LinkedPolynomial(ls)
        other1 = LinkedPolynomial(lo)

        new = []
        
        for x in range(len(self1.polyList)):
            for y in range(len(other1.polyList)):
                new.append(Term(self1.polyList[x].coef * other1.polyList[y].coef, self1.polyList[x].exp + other1.polyList[y].exp))

        
        for x in new:
            for y in new:
                if x.exp==y.exp and new.index(x) != new.index(y):
                    i = new.index(x)
                    new.insert(i, Term(x.coef+y.coef,x.exp))
                    new.remove(x)
                    new.remove(y)
        
        return LinkedPolynomial(new)

                                
