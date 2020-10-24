from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Adding an icon
icon = QIcon("marker.png")

# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Creating the options 
menu = QMenu()
option1 = QAction("Start Server")
# option1.triggered.connect(testFunction)
option2 = QAction("Stop Server") 
menu.addAction(option1)
menu.addAction(option2)

# To quit the app 
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Adding options to the System Tray 
tray.setContextMenu(menu)

def testFunction():
    print("test")

if __name__ == '__main__':
    app.exec_()