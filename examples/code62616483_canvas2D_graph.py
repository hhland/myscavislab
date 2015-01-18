
from java.awt import Color
from java.util import Random
from jhplot  import HGraph

c1 = HGraph("Canvas",600,400,1, 1)
c1.setGTitle("Connected objects")
c1.visible(1)

v1="v1"
v2="v2"
v3="v3"
v4="v4"

c1.addVertex( v1 )
c1.addVertex( v2 )
c1.addVertex( v3 )
c1.addVertex( v4 )

c1.setPos( v1, 130, 40 )
c1.setPos( v2, 60, 200 )
c1.setPos( v3, 310, 230 )
c1.setPos( v4, 380, 70 )

c1.addEdge( v1, v2 )
c1.addEdge( v2, v3 )
c1.addEdge( v3, v1 )
c1.addEdge( v4, v3 )