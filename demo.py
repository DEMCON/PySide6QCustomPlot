
import math

from pyside6qcustomplot import QCustomPlot, QCP
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPen

app = QApplication([])

widget = QCustomPlot()
widget.setWindowTitle("QCustomPlot demo")
widget.setInteractions(QCP.iRangeDrag | QCP.iRangeZoom)
widget.setPlottingHint(QCP.PlottingHint.phFastPolylines, True)
widget.legend.setVisible(True)
widget.show()
widget.resize(800, 600)

g1 = widget.addGraph()
pen1 = QPen(Qt.blue)
pen1.setWidth(3)
g1.setPen(pen1)
g1.setName("First graph")

g2 = widget.addGraph()

pen2 = QPen(Qt.red)
pen2.setWidth(2)
g2.setPen(pen2)
g2.setName("Second graph")

widget.xAxis.setRange(-10, 400)
widget.xAxis.setLabel("Time [s]")
widget.yAxis.setRange(-10, 40)
widget.yAxis.setLabel("Value")

x = [t * 0.01 for t in range(100)]
y = [math.sin(v) for v in x]
y2 = [v+10 for v in y]
g1.setData(x, y)
g2.setData(x, y2)

t = x[-1]
def add_data():
    global t
    x = [t+dt * 0.01 for dt in range(100)]
    t = x[-1]
    
    y = [math.sin(v) for v in x]
    y2 = [v+10 for v in y]
    g1.addData(x, y)
    g2.addData(x, y2)
    widget.replot(QCustomPlot.RefreshPriority.rpQueuedReplot)
    print('data size first graph:', g1.dataCount(), 'replot time:', widget.replotTime())
    

timer = QTimer()
timer.setInterval(60)
timer.timeout.connect(add_data)
timer.start()

app.exec()

