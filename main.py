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

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset =  (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset


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
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel=(4,0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        #bounce off paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        #bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        #ball went to the side, score a point for the corresponding player
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4,0))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4,0))
    #implement on_touch_move function for PongGame class
    #set the position of the left or right player
    #based on whether touch occurred on left or right side of screen
    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

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
