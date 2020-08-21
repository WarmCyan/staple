from staple.graph import Graph
from staple.node import Node

import staple.rendering


# def test():
#     g = Graph()
#     n = Node("Hello")
#     n1 = Node("Test1")
#     n2 = Node("Test2")
# 
#     n.add_activation(n1, .5)
#     n.add_activation(n2, .5)
# 
#     g.nodes = [n, n1, n2]
# 
#     string = staple.rendering.get_graphviz_rep(g)
#     # print(string)
#     display = staple.rendering.render_text_graph(string)
#     print(display)
# 
# test()

g = Graph()

# n = Node("Hello")
# n1 = Node("Test1")
# n2 = Node("Test2")
# 
# n.add_activation(n1, .5)
# n.add_activation(n2, .5)
# 
# g.add_node(n)
# g.add_node(n1)
# g.add_node(n2)


def get_cmd():
    global g
    print("Nodes: ")
    for index, node in enumerate(g.nodes):
        print("\t", index, node.name)
    print("")
    print("1. Add node \t\t'1 NAME'")
    print("2. Add connection \t'2 NODE1 NODE2 WEIGHT' (node1 -> node2)")
    print("3. Change connection \t'3 NODE1 NODE2 WEIGHT'")
    print("4. Delete connection \t'4 NODE1 NODE2'")
    print("5. Delete node \t\t'5 NODE'")
    print("6. Save \t\t6 NAME")
    print("7. Load \t\t7 NAME")
    print("8. Exit")
    return input("> ")

def handle_cmd(command):
    global g
    parts = command.split(" ")

    cmd_index = parts[0]
    
    if cmd_index == "1":
        n = Node(parts[1])
        g.add_node(n)
        return 0
    elif cmd_index == "2":
        index1 = int(parts[1])
        index2 = int(parts[2])
        weight = float(parts[3])

        g.nodes[index2].add_activation(g.nodes[index1], weight)
        return 0
    elif cmd_index == "6":
        name = parts[1]
        g.save(name + ".graph")
        return 0
    elif cmd_index == "7":
        name = parts[1]
        g.load(name + ".graph")
        return 0
    elif cmd_index == "8":
        return 1

while handle_cmd(get_cmd()) != 1:
    string = staple.rendering.get_graphviz_rep(g)
    display = staple.rendering.render_text_graph(string)
    print("\n\n")
    print(display)
    print("\n\n")
