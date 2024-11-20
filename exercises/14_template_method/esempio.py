#versione modificata del codice presente su github (Copyright 2013, Michael H. Goldwasser)
# per essere usato nel libro:
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013

# https://github.com/mjwestcott/Goodrich/blob/master/ch08/linked_binary_tree.py
# il codice poc'anzi linkato è stato scaricato nella cartella 15_factory_method/github ed è stato opportunamente
# modificatoper farlo funzionare correttamente

from github.ch08.linked_binary_tree import LinkedBinaryTree

class BinaryEulerTour():
    def __init__ (self, tree):
        self._tree = tree

    def tree(self):
        return self._tree

    def execute(self):
        if len(self._tree) > 0:
            return self._tour(self._tree.root())

    def _tour(self, p):
        results = [None, None]
        self._previsit(p)
        if self._tree.left(p) is not None:
            results[0] = self._tour(self._tree.left(p))
        self._invisit(p)
        if self._tree.right(p) is not None:
            results[1] = self._tour(self._tree.right(p))
        answer = self._postvisit(p, results)
        return answer

    def   _invisit(self, p): pass
    def   _previsit(self, p): pass
    def   _postvisit(self, p, results): pass


class InorderPrint(BinaryEulerTour):
    def _invisit(self,p):
        print(p.element(),end=" ")

class  SumPostorder(BinaryEulerTour):
    def _postvisit(self, p, results):
        res=p.element()
        if results[0]: res+=results[0]
        if results[1]: res+=results[1]
        return res




tree=LinkedBinaryTree()

root=tree._add_root(1)
lroot=tree._add_left(root,2)
llroot=tree._add_left(lroot,3)
rlroot=tree._add_right(lroot,4)
rroot=tree._add_right(root,5)
lrroot=tree._add_left(rroot,6)

print("\nStampiamo gli elementi dell'albero nell'ordine in cui vengono visitati da una inorder:")
I=InorderPrint(tree)
I.execute()
print("\nOra sommiamo gli elementi dell'albero:")
S=SumPostorder(tree)
print(S.execute())