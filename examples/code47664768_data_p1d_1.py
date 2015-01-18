
from jhplot  import  *
from java.awt import Color

p1=P1D("1st data set")
p1.add(1,2)
p1.add(2,3)
p1.add(4,5)

p2=P1D("2nd data set")
p2.add(-1,3)
p2.add(5,-2)
p2.add(1,0)
p2.setColor(Color.red)

c1 = HPlot("Canvas")
c1.visible()
c1.setAutoRange()

c1.draw(p1)
c1.draw(p2)