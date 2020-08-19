import staple.graph
import staple.util


def get_graphviz_rep(graph):
    """ Return a text version of the graph in graphviz syntax """

    # NOTE: assumes graph-easy is installed

    graphviz_string = "digraph G {"

    for node in graph.nodes:
        graphviz_string += f"\n{node.name}"

    for node in graph.nodes:
        for activation in node.activations:
            graphviz_string += f"\n{activation[0].name} -> {node.name} [label=\"{activation[1]}\"]"

    graphviz_string += "\n}"
    return graphviz_string


def render_text_graph(graphviz_string):
    """ Returns ascii string of graph of passed graphviz_string """

    #with open("./temp_graph.dot", "w") as outfile:
    #    outfile.write(graphviz_string)

    results = staple.util.run_raw_shell(
        f"echo '{graphviz_string}' | graph-easy --as=ascii"
    )

    return results
