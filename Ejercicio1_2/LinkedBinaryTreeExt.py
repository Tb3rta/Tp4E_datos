from typing import Any, List
from Ejercicio1_2.LinkedBinaryTreeExtAbstract import LinkedBinaryTreeExtAbstract
from python_ed_fcad_uner.data_structures import LinkedBinaryTree, BinaryTreeNode


class LinkedBinaryTreeExt(LinkedBinaryTree,LinkedBinaryTreeExtAbstract):
    def hermanos(self, nodo1 : BinaryTreeNode, nodo2: BinaryTreeNode) -> bool: # si son hijo izquierdo e hijo derecho del mismo nodo padre
        pass

    def hojas(self) -> List[Any]:
        pass
    def internos(self) -> List[Any]:
        pass
    def profundidad(self, nodo : BinaryTreeNode) -> int:
        pass
    def altura(self, nodo : BinaryTreeNode) -> int:
        pass

