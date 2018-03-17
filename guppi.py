from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui


import sys


# Create an PyQT4 application object.
a = QApplication(sys.argv)       

# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QWidget()
palette = w.palette()
#w.setBackground(QtGui.QColor('red')) 
palette.setBrush(QPalette.Background,QBrush(QPixmap("page1.png")))
w.setPalette(palette)

# Variables 

sourceFileLoation = ""
destinationFileLocation = ""
currentFileConfig = {

					"sourceFileLocation" : "",
					"destinationFileLocation" : "", 
					"printerFirmware" : "",
					"tipSize" : "",
					"material": ""

					}



# Set window size. 
w.setFixedSize(640, 480)

def selectMaterial():
	print "Select Material"
	print currentFileConfig

def pinkTip():
	currentFileConfig["tipSize"] = {"colour":"PINK", "AWG":"20", "ID":"0.024"}
	selectMaterial()

def blueTip():
	currentFileConfig["tipSize"] = {"colour":"BLUE", "AWG":"22", "ID":"0.017"}
	selectMaterial()

def OrangeTip():
	currentFileConfig["tipSize"] = {"colour":"ORANGE", "AWG":"23", "ID":"0.013"}
	selectMaterial()

def redTip():
	currentFileConfig["tipSize"] = {"colour":"RED", "AWG":"25", "ID":"0.011"}
	selectMaterial()



def selectTip():
	print "Select Tip"
	palette.setBrush(QPalette.Background,QBrush(QPixmap("page5.png")))
	w.setPalette(palette)
	w.show() 
	repeaterBtn.setEnabled(False)
	reprapBtn.setEnabled(False)
	marlinBtn.setEnabled(False)

	pinkTipBtn.setGeometry(QtCore.QRect(37, 80, 125, 427))
	pinkTipBtn.setToolTip('select this Tip')
	pinkTipBtn.setAttribute(QtCore.Qt.WA_TranslucentBackground)
	pinkTipBtn.setStyleSheet("background-color: rgba(0,0,0,0)")
	pinkTipBtn.clicked.connect(pinkTip)
	pinkTipBtn.show()

	blueTipBtn.setGeometry(QtCore.QRect(190, 80, 125, 427))
	blueTipBtn.setToolTip('select this Tip')
	blueTipBtn.setAttribute(QtCore.Qt.WA_TranslucentBackground)
	blueTipBtn.setStyleSheet("background-color: rgba(0,0,0,0)")
	blueTipBtn.clicked.connect(blueTip)
	blueTipBtn.show()

	orangeTipBtn.setGeometry(QtCore.QRect(350, 80, 125, 427))
	orangeTipBtn.setToolTip('select this Tip')
	orangeTipBtn.setAttribute(QtCore.Qt.WA_TranslucentBackground)
	orangeTipBtn.setStyleSheet("background-color: rgba(0,0,0,0)")
	orangeTipBtn.clicked.connect(OrangeTip)
	orangeTipBtn.show()

	redTipBtn.setGeometry(QtCore.QRect(500, 80, 125, 427))
	redTipBtn.setToolTip('select this Tip')
	redTipBtn.setAttribute(QtCore.Qt.WA_TranslucentBackground)
	redTipBtn.setStyleSheet("background-color: rgba(0,0,0,0)")
	redTipBtn.clicked.connect(redTip)
	redTipBtn.show()

	print currentFileConfig



def selectDestination(destinationFileLocation):
	print "Select Destination"
	palette.setBrush(QPalette.Background,QBrush(QPixmap("page4.png")))
	w.setPalette(palette)
	w.show() 

	


	destinationBtn.setEnabled(False)
	repeaterBtn.setGeometry(QtCore.QRect(50, 180, 120, 120))
	repeaterBtn.setToolTip('select Repeater Firmware')
	repeaterBtn.setAttribute(QtCore.Qt.WA_TranslucentBackground)
	repeaterBtn.setStyleSheet("background-color: rgba(0,0,0,0)")
	repeaterBtn.clicked.connect(selectTip)
	repeaterBtn.show()

	
	reprapBtn.setGeometry(QtCore.QRect(260, 180, 120, 120))
	reprapBtn.setToolTip('select Repeater Firmware')
	reprapBtn.setAttribute(QtCore.Qt.WA_TranslucentBackground)
	reprapBtn.setStyleSheet("background-color: rgba(0,0,0,0)")
	reprapBtn.clicked.connect(selectTip)
	reprapBtn.show()

	
	marlinBtn.setGeometry(QtCore.QRect(460, 180, 120, 120))
	marlinBtn.setToolTip('select Repeater Firmware')
	marlinBtn.setAttribute(QtCore.Qt.WA_TranslucentBackground)
	marlinBtn.setStyleSheet("background-color: rgba(0,0,0,0)")
	marlinBtn.clicked.connect(selectTip)
	marlinBtn.show()

	# Open detination file selection window.
	destinationFileLoation = str(QFileDialog.getExistingDirectory(w, 'Open File', '/'))
	print "Destination File location : "  + destinationFileLoation

	currentFileConfig["destinationFileLocation"] = destinationFileLoation

	print currentFileConfig

def selectSource(sourceFileLoation):
	print "Select Source"
	palette.setBrush(QPalette.Background,QBrush(QPixmap("page3.png")))
	w.setPalette(palette)
	w.show() 

	

	sourceBtn.setVisible(False)
	destinationBtn.setGeometry(QtCore.QRect(250, 280, 150, 60))
	destinationBtn.setToolTip('select Destination')
	destinationBtn.setAttribute(QtCore.Qt.WA_TranslucentBackground)
	destinationBtn.setStyleSheet("background-color: rgba(0,0,0,0)")
	destinationBtn.clicked.connect(selectDestination)
	destinationBtn.show()

	# Open source file selection window.
	sourceFileLocation = str(QFileDialog.getOpenFileName(w, 'Open File', '~'))
	print "Source file Selected : " + sourceFileLocation
	currentFileConfig["sourceFileLocation"] = sourceFileLocation
	print "This is config File : " + str(currentFileConfig)

def startprogram():
	
	print " Start Program"
	startBtn.setEnabled(False)
	palette.setBrush(QPalette.Background,QBrush(QPixmap("page2.png")))
	w.setPalette(palette)
	w.show() 

	
	
	sourceBtn.setGeometry(QtCore.QRect(250, 280, 150, 60))
	sourceBtn.setToolTip('select Source Gccode')
	sourceBtn.setAttribute(QtCore.Qt.WA_TranslucentBackground)
	sourceBtn.setStyleSheet("background-color: rgba(0,0,0,0)")
	sourceBtn.clicked.connect(selectSource)
	sourceBtn.show()

	
	

################################ Buttons #################################


# Add an Source  button




# Add an Start  button
startBtn = QPushButton('', w)
startBtn.hide()
sourceBtn = QPushButton('', w)
sourceBtn.hide()
destinationBtn = QPushButton('', w)
destinationBtn.hide()

repeaterBtn = QPushButton('', w)
repeaterBtn.hide()
reprapBtn = QPushButton('', w)
reprapBtn.hide()
marlinBtn = QPushButton('', w)
marlinBtn.hide()

pinkTipBtn = QPushButton('', w)
pinkTipBtn.hide()
blueTipBtn = QPushButton('', w)
blueTipBtn.hide()
orangeTipBtn = QPushButton('', w)
orangeTipBtn.hide()
redTipBtn = QPushButton('', w)
redTipBtn.hide()







startBtn.setGeometry(QtCore.QRect(150, 120, 309.921, 188.976))
startBtn.setToolTip('Start Program')
startBtn.setAttribute(QtCore.Qt.WA_TranslucentBackground)
startBtn.setStyleSheet("background-color: rgba(0,0,0,0)")
startBtn.show()
startBtn.clicked.connect(startprogram)





	









# Set window title  
w.setWindowTitle("Guppi") 

 
# Show window
w.show() 
 
sys.exit(a.exec_())
