from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("White")
        self.penup()        #so that line is'nt seen when ball moves
        self.x_move = 20
        self.y_move = 20
        self.ball_speed = 0.1

    def move(self):
        """
        So that the ball moves to the top right of the screen
        new coord added by 20 pixels as ball should move at appropriate speed
        VERY IMP - 20 pixels added each time will make ball move very quickly
        Therefore time.sleep(0.1) added in main.py to slow down the ball
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    """
    To detect collision with the top and bottom walls
    Not with the side walls as then player would have missed the ball 
    and other player gets a point
    Screen is 600 pixels tall(+300 above and -300 below)
    But ball is 20X20 pixels so +280 and -280
    """

    def bounce_y(self):
        """
        When bouncing of the walls on top and bottom only the y coord will reverse
        Therefore *= -1 so that it will move in same amounts but in the opposite direction
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        When bouncing off the paddles, Only the x coord will reverse unlike
        the case in bouncing of the top and bottom where only y coord changes
        Therefore *= -1 so that it will move in same amounts but in the opposite direction
        """
        self.x_move *= -1
        self.ball_speed *= 0.9      #reducing the time slept so ball appears to move faster

        #increasing ball speed by reducing time slept only for bounce_x as collision with paddle only counted
    def reset_position(self):
        self.home()         #Ball goes back to the centre
        time.sleep(1)       #So that once the ball goes out, it will only appear after 1 second
        self.ball_speed = 0.1   #resetting ball speed back to intial value = 0.1 so that it just doesn't keep increasing
        self.bounce_x()     #So that ball now goes in the opposite direction as before

