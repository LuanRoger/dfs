from main import *
from unittest import TestCase

class GraphTest(TestCase):
    def test_add_nodes_graph(self):
        node1 = Node("1")
        node2 = Node("2")
        node3 = Node("3")
        node4 = Node("4")

        graph = Graph([node1, node2, node3, node4])

        assert len(graph.nodes) == 4
    
    def test_add_adjacents_to_node(self):
        node1 = Node("1")
        node2 = Node("2")
        node3 = Node("3")
        node4 = Node("4")

        node1.addAdjacent(node2)
        node2.addAdjacent(node3)
        node3.addAdjacent(node4)
        node4.addAdjacent(node1)

        assert len(node1.adjacents) == 1
        assert len(node2.adjacents) == 1
        assert len(node3.adjacents) == 1
        assert len(node4.adjacents) == 1
    
    def test_add_adjacents_to_graph(self):
        node1 = Node("1")
        node2 = Node("2")
        node3 = Node("3")
        node4 = Node("4")

        node1.addAdjacent(node2)
        node2.addAdjacent(node3)
        node3.addAdjacent(node4)
        node4.addAdjacent(node1)

        graph = Graph([node1, node2, node3, node4])

        assert len(graph.nodes[0].adjacents) == 1
        assert len(graph.nodes[1].adjacents) == 1
        assert len(graph.nodes[2].adjacents) == 1
        assert len(graph.nodes[3].adjacents) == 1

    def test_node_initialization_defaults(self):
        node = Node("1")
        node2 = Node("2", 2)

        assert node.color == Color.WHITE
        assert node.grayAt == 0
        assert node.blackAt == 0
        assert node.orderValue == None

        assert node2.color == Color.WHITE
        assert node2.grayAt == 0
        assert node2.blackAt == 0
        assert node2.orderValue == 2

    def test_node_order_graph(self):
        node1 = Node("1", 1)
        node2 = Node("2", 2)
        node3 = Node("3", 3)
        node4 = Node("4", 4)

        graph = Graph([node1, node2, node3, node4])

        assert graph.nodes[0].orderValue == 1
        assert graph.nodes[1].orderValue == 2
        assert graph.nodes[2].orderValue == 3
        assert graph.nodes[3].orderValue == 4
    
    def test_node_order_not_ordered_values(self):
        node1 = Node("1", 3)
        node2 = Node("2", 2)
        node3 = Node("3", 1)
        node4 = Node("4", 8)
        node5 = Node("5", 5)
        node6 = Node("6", 4)
        node7 = Node("7", 7)
        node8 = Node("8", 6)

        graph = Graph([node1, node2, node3, node4, node5, node6, node7, node8])

        assert graph.nodes[0].name == "3"
        assert graph.nodes[1].name == "2"
        assert graph.nodes[3].name == "6"
        assert graph.nodes[2].name == "1"
        assert graph.nodes[4].name == "5"
        assert graph.nodes[5].name == "8"
        assert graph.nodes[6].name == "7"
        assert graph.nodes[7].name == "4"
    
    def test_node_order_no_value_numerical(self):
        node1 = Node("1")
        node2 = Node("2")
        node3 = Node("3")
        node4 = Node("4")
        node5 = Node("5")
        node6 = Node("6")
        node7 = Node("7")
        node8 = Node("8")

        graph = Graph([node7, node2, node8, node3, node1, node4, node6, node5])

        assert graph.nodes[0].name == "1"
        assert graph.nodes[1].name == "2"
        assert graph.nodes[2].name == "3"
        assert graph.nodes[3].name == "4"
        assert graph.nodes[4].name == "5"
        assert graph.nodes[5].name == "6"
        assert graph.nodes[6].name == "7"
        assert graph.nodes[7].name == "8"

    def test_node_order_no_value_alphabetical(self):
        nodeA = Node("A")
        nodeB = Node("B")
        nodeC = Node("C")
        nodeD = Node("D")
        nodeE = Node("E")
        nodeF = Node("F")
        nodeG = Node("G")
        nodeH = Node("H")

        graph = Graph([nodeG, nodeB, nodeH, nodeC, nodeA, nodeD, nodeF, nodeE])

        assert graph.nodes[0].name == "A"
        assert graph.nodes[1].name == "B"
        assert graph.nodes[2].name == "C"
        assert graph.nodes[3].name == "D"
        assert graph.nodes[4].name == "E"
        assert graph.nodes[5].name == "F"
        assert graph.nodes[6].name == "G"
        assert graph.nodes[7].name == "H"

    def test_node_order_same_value(self):
        node1 = Node("1", 1)
        node2 = Node("2", 1)
        node3 = Node("3", 1)
        node4 = Node("4", 1)
        node5 = Node("5", 1)
        node6 = Node("6", 1)
        node7 = Node("7", 1)
        node8 = Node("8", 1)

        graph = Graph([node1, node2, node3, node4, node5, node6, node7, node8])

        assert graph.nodes[0].name == "1"
        assert graph.nodes[1].name == "2"
        assert graph.nodes[2].name == "3"
        assert graph.nodes[3].name == "4"
        assert graph.nodes[4].name == "5"
        assert graph.nodes[5].name == "6"
        assert graph.nodes[6].name == "7"
        assert graph.nodes[7].name == "8"

class DfsAlgorithnTest(TestCase):
    def test_dfs_algorithm(self):
        node1 = Node("1", 1)
        node2 = Node("2", 2)
        node3 = Node("3", 3)
        node4 = Node("4", 4)

        node1.addAdjacent(node2)
        node2.addAdjacent(node3)
        node3.addAdjacent(node4)
        node4.addAdjacent(node1)

        graph = Graph([node1, node2, node3, node4])
        dfs(graph)

        assert graph.runDfs == True

        assert graph.nodes[0].color == Color.BLACK
        assert graph.nodes[1].color == Color.BLACK
        assert graph.nodes[2].color == Color.BLACK
        assert graph.nodes[3].color == Color.BLACK

        assert graph.nodes[0].grayAt == 1
        assert graph.nodes[1].grayAt == 2
        assert graph.nodes[2].grayAt == 3
        assert graph.nodes[3].grayAt == 4

        assert graph.nodes[3].blackAt == 5
        assert graph.nodes[2].blackAt == 6
        assert graph.nodes[1].blackAt == 7
        assert graph.nodes[0].blackAt == 8

    def test_graph_black_gray_mark(self):
        nodeC = Node("C", 1)
        nodeA = Node("A", 2)
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

        assert graph.runDfs == True

        assert graph.nodes[0].color == Color.BLACK
        assert graph.nodes[1].color == Color.BLACK
        assert graph.nodes[2].color == Color.BLACK
        assert graph.nodes[3].color == Color.BLACK
        assert graph.nodes[4].color == Color.BLACK
        assert graph.nodes[5].color == Color.BLACK
        assert graph.nodes[6].color == Color.BLACK
        assert graph.nodes[7].color == Color.BLACK

        # Ele começa a pintar os nós a partir do nó C e depois o G, aqui ele pinta o D

    def test_node_edge_kind(self):
        nodeA = Node("A", 1)
        nodeB = Node("B", 2)
        nodeC = Node("C", 3)
        nodeD = Node("D", 4)
        nodeE = Node("E", 5)
        nodeF = Node("F", 6)
        nodeG = Node("G", 7)
        nodeH = Node("H", 8)

        nodeA.addAdjacent(nodeB)
        nodeA.addAdjacent(nodeC)
        nodeA.addAdjacent(nodeF)

        nodeB.addAdjacent(nodeE)

        nodeC.addAdjacent(nodeD)

        nodeD.addAdjacent(nodeA)
        nodeD.addAdjacent(nodeH)

        nodeE.addAdjacent(nodeF)
        nodeE.addAdjacent(nodeG)
        nodeE.addAdjacent(nodeH)

        nodeF.addAdjacent(nodeG)
        nodeF.addAdjacent(nodeB)

        nodeH.addAdjacent(nodeG)

        graph: Graph = Graph([nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH])

        dfs(graph)

        assert graph.runDfs == True

        assert graph.nodes[0].color == Color.BLACK
        assert graph.nodes[1].color == Color.BLACK
        assert graph.nodes[2].color == Color.BLACK
        assert graph.nodes[3].color == Color.BLACK
        assert graph.nodes[4].color == Color.BLACK
        assert graph.nodes[5].color == Color.BLACK
        assert graph.nodes[6].color == Color.BLACK
        assert graph.nodes[7].color == Color.BLACK

        assert graph.nodes[0].edgesKind["B"] == EdgeKind.TREE
        assert graph.nodes[0].edgesKind["C"] == EdgeKind.TREE
        assert graph.nodes[0].edgesKind["F"] == EdgeKind.FORWARD

        assert graph.nodes[1].edgesKind["E"] == EdgeKind.TREE

        assert graph.nodes[2].edgesKind["D"] == EdgeKind.TREE

        assert graph.nodes[3].edgesKind["A"] == EdgeKind.BACK
        assert graph.nodes[3].edgesKind["H"] == EdgeKind.CROSS

        assert graph.nodes[4].edgesKind["F"] == EdgeKind.TREE
        assert graph.nodes[4].edgesKind["G"] == EdgeKind.FORWARD
        assert graph.nodes[4].edgesKind["H"] == EdgeKind.TREE

        assert graph.nodes[5].edgesKind["G"] == EdgeKind.TREE
        assert graph.nodes[5].edgesKind["B"] == EdgeKind.BACK

        assert graph.nodes[7].edgesKind["G"] == EdgeKind.CROSS

    def test_graph_stack(self):
        node0 = Node("0", 0)
        node1 = Node("1", 1)
        node2 = Node("2", 2)
        node3 = Node("3", 3)
        node4 = Node("4", 4)
        node5 = Node("5", 5)
        node6 = Node("6", 6)
        node7 = Node("7", 7)
        node8 = Node("8", 8)
        node9 = Node("9", 9)

        node0.addAdjacent(node1)
        node0.addAdjacent(node2)
        node0.addAdjacent(node3)
        node0.addAdjacent(node5)

        node1.addAdjacent(node2)
        
        node2.addAdjacent(node3)
        node2.addAdjacent(node4)

        node4.addAdjacent(node6)

        node5.addAdjacent(node6)
        node5.addAdjacent(node4)

        node6.addAdjacent(node7)
        node6.addAdjacent(node8)

        node7.addAdjacent(node8)

        node9.addAdjacent(node6)

        graph: Graph = Graph([node0, node1, node2, node3, node4, node5, node6, node7, node8, node9])

        dfs(graph)

        assert graph.runDfs == True

        assert graph.nodes[0].color == Color.BLACK
        assert graph.nodes[1].color == Color.BLACK
        assert graph.nodes[2].color == Color.BLACK
        assert graph.nodes[3].color == Color.BLACK
        assert graph.nodes[4].color == Color.BLACK
        assert graph.nodes[5].color == Color.BLACK
        assert graph.nodes[6].color == Color.BLACK
        assert graph.nodes[7].color == Color.BLACK
        assert graph.nodes[8].color == Color.BLACK
        assert graph.nodes[9].color == Color.BLACK

        assert graph.stack[0] == node3
        assert graph.stack[1] == node8
        assert graph.stack[2] == node7 
        assert graph.stack[3] == node6
        assert graph.stack[4] == node4
        assert graph.stack[5] == node2
        assert graph.stack[6] == node1
        assert graph.stack[7] == node5
        assert graph.stack[8] == node0
        assert graph.stack[9] == node9