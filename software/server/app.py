import sys
from sys import setdlopenflags

# from server import *

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ServerTrayApp():
  def __init__(self):
    # Create a Qt application
    self.app = QApplication(sys.argv)
    
    icon = QIcon("./images/icon.png")
    self.greenIndicator = QIcon("./images/indicator-green.png")
    self.orangeIndicator = QIcon("./images/indicator-orange.png")
    menu = QMenu()
    
    self.statusIndicator = menu.addAction(self.orangeIndicator, "Status: Stopped")
    self.statusIndicator.setDisabled(True)
    
    menu.addSeparator()

    startAction = menu.addAction("Start Server")
    startAction.triggered.connect(self.startServer)

    stopAction = menu.addAction("Stop Server")
    stopAction.triggered.connect(self.stopServer)

    menu.addSeparator()

    exitAction = menu.addAction("exit")
    exitAction.triggered.connect(sys.exit)
    
    self.tray = QSystemTrayIcon()
    self.tray.setIcon(icon)
    self.tray.setContextMenu(menu)
    self.tray.show()
    self.tray.setToolTip("unko!")
    # self.tray.showMessage("hoge", "moge")
    # self.tray.showMessage("fuga", "moge")
    
  def run(self):
    # Enter Qt application main loop
    self.app.exec_()
    sys.exit()

  def serverStatusIndicator(self, status: bool):
    if status:
      self.statusIndicator.setIcon(self.greenIndicator)
      self.statusIndicator.setText("Status: Running")
    else:
      self.statusIndicator.setIcon(self.orangeIndicator)
      self.statusIndicator.setText("Status: Stopped")

  def startServer(self):
    self.serverStatusIndicator(True)

  def stopServer(self):
    self.serverStatusIndicator(False)


if __name__ == "__main__":
  
  # app = QApplication(sys.argv)
  app = ServerTrayApp()
  app.run()