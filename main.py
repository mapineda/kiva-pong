#It is required that the base Class of your Kivy App inherits from the App class
#The uix module is the section that holds the user interface elements like layouts and widgets.
from kivy.app import App
from kivy.uix.widget import Widget
#import properties and vector
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
# import clock and randomint
from kivy.clock import Clock
from random import randint

#define pongpaddle class
class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, bounce):
        if self.collide_widget(ball):
            vx, vy = ball_velocity
            offset =  (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball_velocity = vel.x, vel.y + offset


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
    ball = ObjectProperty(None)

    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(4,0).rotate(randint(0,360))

    def update(self, dt):
        self.ball.move()

        #bounce ball off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
        #bounce ball of left and right
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x += -1

#define base Class for kivy app
#function initializes and returns the Root Widget
class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 6.0)
        return game

#here the class PongApp is initialized and its run() method called. This initializes and starts our Kivy application.
if __name__ == '__main__':
    PongApp().run()
