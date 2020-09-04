import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import Numericproperty,ReferenceListproperty,Objectproperty
from kivy.vector import Vector
from kivy.clock import Clock

class Myball(Widget):
    velocity_x =  NumericProperty(0)
    velocity_y =  NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x,velocity_y)
    def move(self):
        self.pos = Vector(*self.velocity)+self.pos


class Mygame(Widget):
    ball = ObjectProperty(None)
    def update(self,dt):
        self.ball.move()



class Myapp(App):
    def build(self):
        game = Mygame()
        Clock.shedule_interval(game.update,1.0/60.0)
 
if __name__=="__main__":
    Myapp().run()

