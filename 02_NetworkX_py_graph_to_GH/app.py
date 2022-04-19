from flask import Flask
import ghhops_server as hs

import geometry as geo
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/miserables1",
    name = "Create Graph Miserables",
    inputs=[],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST)
    ]
)

def miserables():
    nodes = geo.miserables()[0]
    edges = geo.miserables()[1]
    return nodes, edges

if __name__== "__main__":
    app.run(debug=True)