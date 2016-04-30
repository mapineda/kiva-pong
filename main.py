#It is required that the base Class of your Kivy App inherits from the App class
#The uix module is the section that holds the user interface elements like layouts and widgets.
from kivy.app import App
from kivy.uix.widget import Widget
#add imports from property class and vector
from kivy.property import NumericProperty, ReferenceListProperty
from kivy.vector import Vector



#define the ball
class PongBall(Widget):

    #velocity of ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    #referencelist property so we can use ball.velocity as
    #shorthand, e.g w.pos, x.pos, w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    #"move" function will move the ball one step.
    #this will be called in equal intervals to animate the ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

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
