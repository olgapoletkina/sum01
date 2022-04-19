import rhino3dm as rg
import networkx as nx
from flask import Flask
import ghhops_server as hs

app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/movepoints",
    name = "MovePoints",
    inputs=[
        hs.HopsPoint("Points", "Pts", "Add points", hs.HopsParamAccess.LIST),
        hs.HopsInteger('Integer X', 'X_Int', 'Distance X',hs.HopsParamAccess.ITEM, default=10),
        hs.HopsInteger('Integer Y', 'Y_Int', 'Distance Y',hs.HopsParamAccess.ITEM, default=10),
        hs.HopsInteger('Integer Z', 'Z_Int', 'Distance Z',hs.HopsParamAccess.ITEM, default=10)
    ],
    outputs=[
       hs.HopsPoint("Points", "Pts", "Add points", hs.HopsParamAccess.LIST)
    ]
)

def movePoints(points,X, Y,Z):
    moved_points=[]
    for i in points:
        moved_point=rg.Point3d(X+i.X, Y+i.Y, Z+i.Z)
        moved_points.append(moved_point)
    return moved_points

#def movepoints(points, Y):
    #ptsmoved = []
    #for p in points:
        #p = rg.Point3d(0,Y,0)
        #ptsmoved.append(p)
    #return(ptsmoved)

if __name__== "__main__":
    app.run(debug=True)
