import random


class red():
    def __init__(self,red,blue):
        self.red = red
        self.blue = blue

    def order(self):
        red_ball_list= random.sample(range(1,self.red+1), 6)
        blue_ball_list = random.sample(range(1, self.blue+1), 1)
        red_ball_list=sorted(red_ball_list)
        double=red_ball_list+ blue_ball_list
        print (double)


ball=red(32,16)
ball.order()
