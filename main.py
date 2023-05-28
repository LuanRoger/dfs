from enum import Enum
from typing import Dict, List, Optional

class Color(Enum):
	WHITE = 0
	GRAY = 1
	BLACK = 2
	
class EdgeKind(Enum):
	TREE = 0
	FORWARD = 1
	BACK = 2
	CROSS = 3

	def __str__(self):
		if self == EdgeKind.TREE:
			return "Arvore"
		elif self == EdgeKind.FORWARD:
			return "Avanço"
		elif self == EdgeKind.BACK:
			return "Retorno"
		elif self == EdgeKind.CROSS:
			return "Cruzamento"
		return "<!>"

class Node:
	def __init__(self, name: str, orderValue: Optional[int] = None):
		self.orderValue = orderValue
		self.adjacents = []
		self.edgesKind: Dict[str, EdgeKind] = {}
		self.name = name
		self.grayAt = 0
		self.blackAt = 0
		self.color = Color.WHITE

	def addAdjacent(self, node):
		self.adjacents.append(node)
	
	def __str__(self):
		return self.name

class Graph:
	def __init__(self, nodes: List[Node]):
		self.nodes: List[Node] = nodes
		self.mark = 0
		self.orderNodes()
		self.stack = []
		self.runDfs = False
	
	def hasNodeWithValue(self) -> bool:
		for node in self.nodes:
			if node.orderValue is not None:
				return True
		return False

	def printStack(self):
		print('Stack: [', end=' ')
		for node in self.stack:
			print(node.name, end=' ')
		print(']')

	def printListAdjacents(self):
		for node in self.nodes:
			print(f"{node.name}({node.grayAt}/{node.blackAt})", end=': ')
			for adjacent in node.adjacents:
				print(adjacent.name, end=' ')
			print()
	
	def printNodesEdgesKind(self):
		for node in self.nodes:
			for adjacent in node.adjacents:
				print(f"{node.name} -- {str(node.edgesKind[adjacent.name])} --> {adjacent.name}")
	
	def orderNodes(self):
		if not self.hasNodeWithValue():
			self.nodes = sorted(self.nodes, key=lambda node: node.name)
			return
		
		for node in self.nodes:
			if node.orderValue is None:
				print('Error: Node without order value')
				return
		self.nodes = sorted(self.nodes, key=lambda node: node.orderValue) # type: ignore


def dfs(graph: Graph):
	for node in graph.nodes:
		if node.color == Color.WHITE:
			dfs_visit(graph, node)
	graph.runDfs = True

def dfs_visit(graph: Graph, node: Node):
	node.color = Color.GRAY
	graph.mark += 1
	node.grayAt = graph.mark

	for neighbour in node.adjacents:
		if neighbour.color == Color.WHITE:
			node.edgesKind[neighbour.name] = EdgeKind.TREE
			dfs_visit(graph, neighbour)
		elif neighbour.color == Color.GRAY:
			node.edgesKind[neighbour.name] = EdgeKind.BACK
		elif neighbour.color == Color.BLACK and node.grayAt < neighbour.grayAt:
			node.edgesKind[neighbour.name] = EdgeKind.FORWARD
		elif neighbour.color == Color.BLACK and node.grayAt > neighbour.grayAt:
			node.edgesKind[neighbour.name] = EdgeKind.CROSS

	node.color = Color.BLACK
	graph.mark += 1
	node.blackAt = graph.mark
	graph.stack.append(node)

if __name__ == '__main__':
	nodeA = Node("A", 2)
	nodeC = Node("C", 1)
	nodeB = Node("B", 3)
	nodeD = Node("D", 4)
	nodeE = Node("E", 5)
	nodeF = Node("F", 6)
	nodeG = Node("G", 7)
	nodeH = Node("H", 8)

	nodeA.addAdjacent(nodeB)

	nodeB.addAdjacent(nodeC)
	nodeB.addAdjacent(nodeE)
	nodeB.addAdjacent(nodeF)

	nodeC.addAdjacent(nodeD)
	nodeC.addAdjacent(nodeG)

	nodeD.addAdjacent(nodeC)
	nodeD.addAdjacent(nodeH)

	nodeE.addAdjacent(nodeA)
	nodeE.addAdjacent(nodeF)

	nodeF.addAdjacent(nodeG)

	nodeG.addAdjacent(nodeF)
	nodeG.addAdjacent(nodeH)

	nodeH.addAdjacent(nodeH)

	graph: Graph = Graph([nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH])

	dfs(graph)

	print("Tipos de arestas:")
	graph.printNodesEdgesKind()

	print("Lista de adjacências:")
	graph.printListAdjacents()

	print("Ordem topológica:")
	graph.printStack()