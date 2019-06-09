import sys
sys.setrecursionlimit(100000)

def factorial(n):
# Provide your code here
    if n == 1 or n == 0:
        return 1
    else:
        return factorial(n-1)*n

print "factorial(5):", factorial(5)
# Expected 120
print


def fib(n):
# Provide your code here
    if n <= 1:
        return n
    else:
        return (fib(n-1)+fib(n-2))

print "fib(7):", fib(7)
# Expected 13
print

def equal(A, B):
# Provide your code here
    if A == B:
        return "True"
    else:
        return "False"


print "equal('ALICE', 'BOB):", equal('ALICE', 'BOB')
# Expected False
print "equal('ALICE', 'ALICE'):", equal('ALICE', 'ALICE')
# Expected True
print

def addup(list):
    total = 0
    for x in list:
        total += x
    return total
# Provide your code here

print "addup([1,2,3,4,5]):", addup([1,2,3,4,5])
# Expected 15
print "addup(range(101)):", addup(range(101))
# Expected 5050
print


def reverse(A):
# Provide your code here
    return A[::-1]

print "reverse('hello'):", reverse('hello')
# Expected olleh

print

def isSorted(list):
# Provide your code here
    list1=list[:]
    list1.sort()
    if (list==list1):
        return "True"
    else:
        return "False"

print "isSorted([1,2,3,4]):", isSorted([1,2,3,4])
# Expected True
print "isSorted([1,22,3,4]):", isSorted([1,22,3,4])
# Expected False

print

def linearSearch(A, value):
# Provide your code here
    found = False
    position = 0
    while position < len(A) and not found:
        if A[position] == value:
            found = True
        position = position + 1
    return found

print "linearSearch([1, 2, 3, 4, 5], 4):", linearSearch([1, 2, 3, 4, 5], 4)
# Expected True
print "linearSearch(range(900), -1):", linearSearch(range(900), -1)
# Expected False

print

def binarySearch(A, value):
# Provide your code here
    right_end = len(A)-1
    left_end = 0
    while left_end <= right_end:
        mid = left_end + (right_end - left_end)/2
        if A[mid] == value:
            return "True"
        elif A[mid] < value:
            left_end = mid + 1
        else:
            right_end = mid - 1
            return "False"

print "binarySearch([1, 2, 3, 4, 5], 4):", binarySearch([1, 2, 3, 4, 5], 4)
# Expected True
print "binarySearch(range(1000000), -1):", binarySearch(range(1000000), -1)
# Expected False
print
