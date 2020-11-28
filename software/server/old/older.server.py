import time
import rumps

rumps.debug_mode(True)

class ServerApp(object):
  def __init__(self):
    self.config = {
      "app_name": "PiDeck Server",
      "start": "Start Server",
      "stop": "Stop Server"
    }
      
    #Declaration of rumps.app as app
    self.app = rumps.App(self.config["app_name"])
    self.app.title = "🍅"
    # self.app.icon = ""

    self.initalStatus = "please wait..."

    self.status_indicator = rumps.MenuItem(title='Status: {}'.format(self.initalStatus), callback=None)
    self.start_button = rumps.MenuItem(title=self.config["start"], callback=None)
    self.stop_button = rumps.MenuItem(title=self.config["stop"], callback=None)
    self.app.menu = [self.status_indicator, None, self.start_button, self.stop_button, None]


def serverStatus():
  time.sleep(5)
  status_indicator.title = "running"

def checkServerStatus():
  return "running"
    
def run():
  self.app.run()


if __name__ == '__main__':
  app = ServerApp()
  app.run()