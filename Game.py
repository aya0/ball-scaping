from pygame import Vector2

from Ball import Ball
from Utils import utils

# add funcions to method
class Game:
    
    def __init__(self):
        self.ball = Ball(Vector2(utils.width/2, utils.height/2) , 2 ,(255,255,255))
    
    def update(self):
        utils.world.Step(1.0 / 60.0 , 6 ,2)
    
    def draw(self):
        self.ball.draw()
    