from graphviz import Digraph
import settings


def draw_graf():
    nodes = settings.list_of_nodes
    edges = settings.list_of_edges
    dot = Digraph(comment='The TreeSong Table')
    add_node(dot, nodes)
    dot.view()
    dot.edges(edges)
    print(dot.source)
    # dot.view()
    dot.render('test-output/TreeSong.gv', view=True)


def add_node(dot, nodes):
    for i in range(len(nodes)):
        dot.node(nodes[i].name, f'Dot {nodes[i].info}')