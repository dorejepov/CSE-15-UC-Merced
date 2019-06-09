from logic import TruthTable

pro1 = raw_input("Enter Proposition 1:\n")

pro2 = raw_input("Enter Proposition 2:\n")


notTable = TruthTable(['p'] , ['-p'])
notTable.display()
print notTable.table

not1Table = TruthTable(['q'] , ['-q'])
not1Table.display()
print not1Table.table

print ""

yesTable = TruthTable(['p' , 'q'] , ['p and q'])
yesTable.display()

print ""

ONETable = TruthTable(['p' , 'q'] , ['p or q'])
ONETable.display()

print ""

TWOTable = TruthTable(['p' , 'q'] , ['p -> q'])
TWOTable.display()

print ""

THREETable = TruthTable(['p' , 'q'] , ['p <-> q'])
THREETable.display()


print 'The Proposition are equivalent'

else:
   print 'The Proposition are not equivalent'
