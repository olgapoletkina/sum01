import rhino3dm as rg
import networkx as nx


def miserables():

    m = nx.les_miserables_graph()
    #lay = nx.kamada_kawai_layout(m)
    lay = nx.circular_layout(m, scale=10, dim=2)
    #lay = nx.shell_layout(m)
    #lay = nx.random_layout(m)

    nodes = []
    for n in lay.values():
        pt = rg.Point3d(n[0], n[1] , 0)
        nodes.append(pt)
        
    edges = []
    for e in m.edges:
        p1 = rg.Point3d( lay[e[0]][0], lay[e[0]][1], 0 )
        p2 = rg.Point3d( lay[e[1]][0], lay[e[1]][1], 0 )
        line = rg.LineCurve(p1, p2)
        edges.append(line)
    return nodes, edges