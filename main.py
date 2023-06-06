from enum import Enum
import sys
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
		print("[", end=' ')
		for node in self.stack:
			print(node.name, end=' ')
		print("]")

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
			heigherExits = 0
			heigherExitsNode: Node = None
			for _, element in enumerate(self.nodes):
				if(len(element.adjacents) > heigherExits):
					heigherExits = len(element.adjacents)
					heigherExitsNode = element
			if heigherExitsNode is not None:
				self.nodes.remove(heigherExitsNode)
				self.nodes.insert(0, heigherExitsNode)
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

def load_graph_from_file(file_path: str) -> Graph:
	with open(file_path, 'r') as file:
		lines = file.readlines()

	nodes: List[Node] = []
	for line in lines:
		line = line.strip()
		node_source_name, node_destiny_name = line.split(' ')


		node_source: Optional[Node] = None
		node_destiny: Optional[Node] = None
		# Checa se os nós já existem
		for node in nodes:
			if node.name == node_source_name:
				node_source = node
			if node.name == node_destiny_name:
				node_destiny = node

		if node_destiny is None:
			node_destiny = Node(node_destiny_name)
			nodes.append(node_destiny)
		if node_source is None:
			node_source = Node(node_source_name)
			nodes.append(node_source)

		node_source.addAdjacent(node_destiny)

	graph: Graph = Graph(nodes)
	return graph

if __name__ == '__main__':
	graph_file_name: Optional[str] = None
	try:
		graph_file_name = sys.argv[1]
	except IndexError:
		print('Error: Arquivo de entrada não informado. Passe o caminho do arquivo como argumento.')
		sys.exit(1)
	graph = load_graph_from_file(graph_file_name)

	dfs(graph)

	print("Tipos de arestas:")
	graph.printNodesEdgesKind()

	print("Lista de adjacências:")
	graph.printListAdjacents()

	print("Ordem topológica:")
	graph.printStack()