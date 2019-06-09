# Exercise 1: Implement Euclid's Algorithm for finding the greatest common divisor of two integers
def gcd(a, b):
    x = a
    y = b

    while (y != 0):
        r = x % y
        x = y
        y = r

    return x
# Provide the correct implementation



print gcd(128, 60)
# Expected output: 4


# Exercise 2: Consider the following representation of mathematical expressions: a list of tuples, where each tuple has exactly 2 elements, a coefficient and a term. For example, the expression:
# 2x + 5y - 3z is represented as [(2, x), (5, y), (-3, z)]
# We sometimes need to simplify expressions by grouping together like terms. For example:
# 2x + 5y + 4x = 6x + 5y
# Implement the function groupLikeTerms, where the input exp is a mathematical expression represented as a list of tuples, and it should return a simplified mathematical expression represented as a list of tuples.
def groupLikeTerms(exp):
# Provide the correct implementation
    newList = []
    for i in range(0, len(exp)):
        newSum = exp[i][0]
        newLetter = exp[i][1]

        for j in range(i + 1, len(exp)):
            if(exp[i][1] == exp[j][1]):
                newSum += exp[j][0]

        tuple = (newSum, newLetter)


        k = i - 1
        doNotInclude = False
        while(k >= 0):
            if(exp[i][1] == exp[k][1]):
                doNotInclude = True
            k = k - 1
        if(doNotInclude == False):
             newList.append(tuple)
    return newList
    #return exp

print groupLikeTerms([(5, "x"), (5, "y"), (-3, "x")])
# Expected output: [(2, 'x'), (5, 'y')]


# Exercise 3: We sometimes need to substitute expressions into other expressions. For example if we have the expression 2x + 5y, and we know that x = 3a - b, we can substitute the expression for x into the original expression, resulting in: 6a - 2b + 5y.
# Implement the substitution function below. It should take an expression (list of tuples), a term, and another expression. It should substitute the occurences of term in exp, with value. The result should be in its simplest form, i.e. like terms should be grouped together
# For example: substitute([(2, 5), (-1, 9)], 5, [(1, 23), (-2, 9)]) results in [(-5, 9), (2, 23)]
def substitute(exp, term, value):
    # Provide the correct implementation
    newList = []

    for i in range(0, len(exp)):
        a = exp[i][0]
        b = exp[i][1]

        if(b == term):
            for j in range(0, len(value)):
                alpha = a * value[j][0]

                tuple = (alpha, value[j][1])
                newList.append(tuple)
        else:
            tuple = (a, b)
            newList.append(tuple)
    return(groupLikeTerms(newList))
    #return exp, value

print substitute([(2, 5), (-1, 9)], 5, [(1, 23), (-2, 9)])
# Expected output: [(-5, 9), (2, 23)]



# Exercise 4: Using the functions you implemented above, implement the Extended Euclidean Algorithm, which returns the GCD of two integers a, and b, as a linear combination of a and b.
# For example: extended_euclid(101, 23) results in (1, [(22, 23), (-5, 101)]), where the GCD is 1 and it can be expressed as 22*23 - 5*101
def extended_euclid(a, b):

    list = []
    x = a
    y = b

    s = 0
    t = 1

    lasts = 1
    lastt = 0

    while (y != 0):
        q = x / y
        r = x % y
        x = y
        y = r

        temp = s
        s = lasts - q * s
        lasts = temp


        temp = t
        t = lastt - t * q
        lastt = temp

        tuple1 = (lasts, a)
        tuple2 = (lastt, b)

        list.append(tuple1)
        list.append(tuple2)

        return gcd(a,b), list
    #return a, []

# Provide the correct implementation

print extended_euclid(101, 23)
# Expected output: (1, [(22, 23), (-5, 101)])



# Exercise 5: Use the Extended Euclidean Algorithm to implement the function for multiplicative inverses. As you know, a multiplicative inverse n modulo m is guaranteed to exist if n and m are relatively prime. If they are not, your algorithm should return None (which is the null value of Python), otherwise, if n and m are relatively prime, you should return the inverse of n modulo m.
def inverse(n, m):
    if (gcd(n,m) != 1):
        return None

    eeResult = extended_euclid(n,m)

    if(eeResult[1][0][0] > 0):
        finalResult = eeResult[1][0][0]
    else:
        finalResult = eeResult[1][1][0]
    return finalResult

    # Provide the correct implementation
    #return n

print inverse(23, 101)
# Expected output: 22

    for i in range(1,m):
        if(m * i + 1) % n == 0:
            return (m * i + 1) // a
            return None

def gcd(i,j):
    while j:
        i,j = j,i % j
        return i

a = input("Input a number of \"a\": ")
b = input("Input a number of \"b\": ")


print("The Greatest Common Divisor of %s and %s is %s" % (a, b, gcd(a,b)))
print("The Modular inverses of %s modulo %s is %s" % (a, b, inverse(a,b)))
