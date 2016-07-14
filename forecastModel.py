import sys
from PyQt4 import QtGui
import matplotlib.pyplot as plt
import pylab
##import oz_drop_down
##import test1


#### subwindow for sending an email...
class Example_mail(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setGeometry(20, 40, 1550, 950)
        self.setWindowIcon(QtGui.QIcon("sdsu.png"))
        self.setWindowTitle("Energy Forecasting")
        self.show()



#### MAIN WINDOW.....
class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()

        
        
    def initUI(self):
        
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 30))
        
        btn = QtGui.QPushButton('Select ', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(100, 50)
        btn.move(50, 50)

        # "QUIT" button to close the application
        btn_quit = QtGui.QPushButton('QUIT', self)
        btn_quit.clicked.connect(self.close) 
        btn_quit.resize(100, 40)
        btn_quit.move(1375, 650)


        # "FORECAST" button for showing the graph
        btn_frcst = QtGui.QPushButton('FORECAST', self)
        btn_frcst.clicked.connect(self.graph)
        btn_frcst.resize(100, 40)
        btn_frcst.move(1250, 650)

        #"SEND EMAIL" button for sending a feedback to someone...
        btn_mail = QtGui.QPushButton('SEND EMAIL', self)
        btn_mail.clicked.connect(self.mail)
        btn_mail.resize(100, 40)
        btn_mail.move(1120, 650)

        #dialogue box for sending an email
    
        


        #label for building drop down...
        
        self.lbl_d_down = QtGui.QLabel("Select Building:", self)
        self.lbl_d_down.move(50, 150)

        #drop down menu for different buildings..
        combo = QtGui.QComboBox(self)
        combo.addItem("Choos a building")
        combo.addItem("Adams Humanities")
        combo.addItem("Engineering")
        combo.addItem("Geology and Computer Science")
        combo.addItem("Student Services East")
        combo.addItem("Student Services West")

        combo.move(50, 170)
        combo.resize(250, 40)
        


        # parameters of a window...
        self.setGeometry(20, 40, 1550, 700)
        self.setWindowIcon(QtGui.QIcon("sdsu.png"))
        self.setWindowTitle("Energy Forecasting")

        self.show()

    def mail(self):
        app1 = QtGui.QApplication(sys.argv)
        ex1 = Example_mail()
        sys.exit(app.exec_())

    def graph(self):
        lst1 = [1,2,3,4]
        lst2 = [1,2,3,4]
        pylab.plot(lst1, lst2)
        pylab.ion()
        pylab.show()


    #def drop_down(self):

# class for calendar....


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
