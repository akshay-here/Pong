from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("PONG")
screen.tracer(0)        #turning off animation

#Creating all the required objects
r_paddle = Paddle((380, 0), "red")
l_paddle = Paddle((-380, 0), "Blue")
ball = Ball()
score = Score()


screen.listen()
screen.onkey(key='Up', fun=r_paddle.move_up)
screen.onkey(key='Down', fun=r_paddle.move_down)
screen.onkey(key='w', fun=l_paddle.move_up)
screen.onkey(key='s', fun=l_paddle.move_down)


should_continue = True
while should_continue:
    time.sleep(ball.ball_speed)     #To slow down the ball
    screen.update()     #Manually updating the screen
    ball.move()
    """
    To detect collision with the top and bottom walls
    Not with the side walls as then player would have missed the ball 
    and other player gets a point
    Screen is 600 pixels tall(+300 above and -300 below)
    But ball is 20X20 pixels so +280 and -280
    """
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
    """
    To detect collision with the paddles 
    have to check distance from ball and paddle and  ake sure its not more than 80 pixels
    80 pixels so that even if ball hits edge of the paddle still considered collision
    also if the ball has moved past x=+350 then it has collided with r_paddle
    also if the ball has moved past x=-350 then it has collided with l_paddle
    Also increase speed of the ball everytime collision with paddle happens to make it challenging 
    This is done by decreasing the time.sleep(n) everytime
    """
    #right paddle collision
    if ball.distance(r_paddle) < 80 and ball.xcor() > 340:
        ball.bounce_x()
        r_paddle.paddle_speed *= 0.9        #reducing time slept so that r_paddle moves faster after every hit

    #left paddle collision
    if ball.distance(l_paddle) < 80 and ball.xcor() < -340:
        ball.bounce_x()
        l_paddle.paddle_speed *= 0.9        #reducing time slept so that l_paddle moves faster after every hit

    """
    To detect if the paddle has missed the ball
    if ball xcor > 380 and distance between ball and r_paddle > 80 then r_paddle has missed
    if ball xcor < -380 and distance between ball and l_paddle > 80 then l_paddle has missed
    if the ball has missed either paddle then ball has to come back to the centre and start to go in the opposite 
    direction so that other paddle then gets a go
    """
    #if right paddle has missed
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()     #left gets point if right paddle misses

    #if left paddle has missed
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()     #right gets point if left paddle misses

screen.exitonclick()