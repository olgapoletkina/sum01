from re import M
from flask import Flask
import ghhops_server as hs
import rhino3dm as rg
import networkx as nx

app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/miserables_n",
    name = "Create Graph Miserables N",
    inputs=[],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       #hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST)
    ]
)
def miserables_n():
    m = nx.les_miserables_graph()
    lay = nx.kamada_kawai_layout(m)
    #lay = nx.circular_layout(m, scale=10, dim=2)
    #lay = nx.shell_layout(m)
    #lay = nx.random_layout(m)
    nodes = []
    for n in lay.values():
        pt = rg.Point3d(n[0], n[1] , 0)
        nodes.append(pt)
    return nodes

@hops.component(
    "/miserables_e",
    name = "Create Graph Miserables E",
    inputs=[],
    outputs=[
       #hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST)
    ]
)
def miserables_e():
    m = nx.les_miserables_graph()
    #lay = nx.kamada_kawai_layout(m)
    lay = nx.circular_layout(m, scale=10, dim=2)
    #lay = nx.shell_layout(m)
    #lay = nx.random_layout(m)
    edges = []
    for e in m.edges:
        p1 = rg.Point3d( lay[e[0]][0], lay[e[0]][1], 0 )
        p2 = rg.Point3d( lay[e[1]][0], lay[e[1]][1], 0 )
        line = rg.LineCurve(p1, p2)
        edges.append(line)
    return edges
    


if __name__== "__main__":
    app.run(debug=True)