from logic import TruthTable

FourTable = TruthTable(['p' , 'q'] ,['p and q' , 'p or -q'])
FourTable.display()

print ""

FourTable.latex()

print ""

FiveTable = TruthTable(['p' , 'q'] , ['p or q' , '-p or -q'])
FiveTable.display()

print ""

FiveTable.latex()

print ""

SixTable = TruthTable(['p' , 'q'] ,['p -> q' , '-q -> -p'])
SixTable.display()

print ""

SixTable.latex()

print ""

SevenTable = TruthTable(['p' , 'q'] ,['p -> q' , '-p or q'])
SevenTable.display()

print ""

SevenTable.latex()

print ""

EightTable = TruthTable(['p' , 'q'] ,['-(p and q)' , '-p or -q'])
EightTable.display()

print ""

EightTable.latex()

print ""
