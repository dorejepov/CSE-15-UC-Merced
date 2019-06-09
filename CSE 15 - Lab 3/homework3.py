from logic import TruthTable

NextTable = TruthTable(['q -> r' ,'p -> (q -> r)'])
NextTable.display()
NextTable.latex()

TheTable = TruthTable(['p and q','(p and q) -> r'])
TheTable.display()
TheTable.latex()

NoTable = TruthTable(['q -> r', 'p -> (q -> r)'])
NoTable.display()
NoTable.latex()

YesTable = TruthTable(['p -> q', '(p -> q) -> r'])
YesTable.display()
YesTable.latex()
