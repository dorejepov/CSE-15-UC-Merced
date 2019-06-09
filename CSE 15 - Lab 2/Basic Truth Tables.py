from logic import TruthTable

notTable = TruthTable(['a'] , ['-a'])
notTable.display()

print ""

yesTable = TruthTable(['a' , 'b'] , ['a and b'])
yesTable.display()

print ""

ONETable = TruthTable(['a' , 'b'] , ['a or b'])
ONETable.display()

print ""

TWOTable = TruthTable(['a' , 'b'] , ['a -> b'])
TWOTable.display()

print ""

THREETable = TruthTable(['a' , 'b'] , ['a <-> b'])
THREETable.display()
