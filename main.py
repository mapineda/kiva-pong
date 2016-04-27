#It’s required that the base Class of your Kivy App inherits from the App class
#The uix module is the section that holds the user interface elements like layouts and widgets.
from kivy.app import App
from kivy.uix.widget import Widget

class PongGame(Widget):
    pass
#define base Class for kivy app
#function initializes and returns the Root Widget
class PongApp(App):
    def build(self):
        return PongGame()
#here the class PongApp is initialized and its run() method called. This initializes and starts our Kivy application.
if __name__ == '__main__':
    PongApp().run()
