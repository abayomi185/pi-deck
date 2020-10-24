import sys
import signal
import os
import argparse

import socket

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class SystemTrayIcon(QSystemTrayIcon):

    def __init__(self, icon, altIcon, exe, parent=None):
        self.icons = {
            'main': QIcon(icon),
            'alt': QIcon(altIcon),
        }

        # Init SystemTrayIcon
        QSystemTrayIcon.__init__(self, self.icons['main'], parent)

        self.onclick_exec=exe

        self.blinker = QTimer()
        self.blinker.timeout.connect(self.blink)

        # Add signal handler for button click
        self.activated.connect(self.onTrayIconActivated)
        
        # Create signal handlers for menu
        self.createActions()

        # Add menu and set signal handler for mouse clicks
        menu = QMenu(parent)
        exitAction = menu.addAction(self.quitAction)
        self.setContextMenu(menu)

        def __getitem__(self, key):
            return self.icons[key]

    def createActions(self):
        self.quitAction = QAction("&Quit", self,
                triggered=qApp.quit)

    def onTrayIconActivated(self, reason):
        # If any click other than a right click
        if reason != QSystemTrayIcon.Context:
            process = QProcess()
            process.startDetached( self.onclick_exec )
            self.stopBlink()

    def blink(self):
        QTimer().singleShot(500, lambda: self.setIcon(self.icons['alt']))
        QTimer().singleShot(1000, lambda: self.setIcon(self.icons['main']))

    def stopBlink(self):
        if self.blinker.isActive():
            self.blinker.stop()

    def sigUSR1(self, signum, frame):
        if not self.blinker.isActive():
            self.blinker.start(1000)

    def sigUSR2(self, signum, frame):
        if self.blinker.isActive():
            self.blinker.stop()

def main():
    app = QApplication(sys.argv)

    widget = QWidget()

    # # Create tray icon with primary and secondary icons
    # trayIcon = SystemTrayIcon(args.icon_path, args.alt_icon_path,
    #         args.onclick_exec, widget)

    # # Register signal handler to trigger blinking
    # signal.signal(signal.SIGUSR1, trayIcon.sigUSR1)
    
    # # Register signal handler to stop blinking
    # signal.signal(signal.SIGUSR2, trayIcon.sigUSR2)
    
    # trayIcon.show()

    # Hack to interrupt Qt
    timer = QTimer()
    timer.timeout.connect(lambda: None)  # Let the interpreter run each 500 ms.
    timer.start(500)  # You may change this if you wish.

    sys.exit(app.exec_())

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument("pidfile", help="Path to save our PID")
    # parser.add_argument("icon_path", help="Path to primary icon")
    # parser.add_argument("alt_icon_path", help="Path to icon to emulate"\
    #         "blinking")
    # parser.add_argument("onclick_exec", nargs='?', help="Command to execute"\
    #         "on mouse click", default="")
    # args = parser.parse_args()

    # # Write PID so caller can send SIGUSR1 to us
    # pidfile = open(args.pidfile, 'w')
    # pidfile.write(str(os.getpid()))
    # pidfile.close()

    # Abort normally for SIGINT
    # signal.signal(signal.SIGINT, signal.SIG_DFL)

    main()