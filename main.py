from turtle import *
import random
#### CLASS AND FUNCTION DEFINITIONS #####
def playing_area():
	t = Turtle()
	t.speed(0)
	t.ht()
	t.pu()
	t.goto(-250,250)
	t.color("light blue")
	t.pd()
	t.begin_fill()
	for i in range(4):
		t.forward(500)
		t.right(90)
	t.end_fill()

# def up():
#     global player
#     player.setheading(90)
#     if player.ycor()!=240:
#         player.sety(player.ycor()+10)
    
# def down():
#     global player
#     player.setheading(-90)
#     if player.ycor()!=-240:
#       player.sety(player.ycor()-10)

class Zombie(Turtle):
    def __init__(self, player):
        super().__init__()
        self.ht()
        self.speed(2)
        self.color("green")
        self.penup()
        self.goto(x,y)
        self.setheading(self.towards(player))
        self.shape("turtle")
        self.player = player

    def move(self):
        self.setheading(self.towards(self.player))
        self.forward(3)	
'''
Player() Class

Constructor( def __init__(self)):
- player should be shaped like a turtle.
- will take in the x and y coordinates for where the player will initially appear.
- will take in a color for the player
- will take in keys to turn left, turn right and shoot bullets.
- player will have an attribute that is a list that stores bullets

move(self):
- moves object forward five pixels

fire(self):
- creates a Bullet object
- appends the Bullet object to the players's bullet list
'''
class Player(Turtle):
    def __init__(self, x, y, color, screen, right_key, left_key, fire_key):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(color)
        self.penup()
        self.goto(x,y)
        self.setheading(90)
        self.shape("turtle")
        self.bullets = []
        self.color = color
        self.alive = True
        self.st()
        screen.onkeypress(self.left, left_key)
        screen.onkeypress(self.right, right_key)
        screen.onkey(self.fire, fire_key)

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

    def move(self):
        self.forward(4)
        if self.xcor() > 230 or self.xcor() < -230:
            self.setheading(180 - self.heading())
        if self.ycor() > 230 or self.ycor() < -230:
            self.setheading(-self.heading())

    def fire(self):
        self.bullets.append(Bullet(self))

    def move_heading(t,zombies):
        self.forward(5)
        if self.xcor() > 240 or self.xcor() < -240:
            self.setheading(180-self.heading())
            self.forward(12)
            Zombie.append(zombies())
        if self.ycor()> 240 or self.ycor()<-240:
            self.setheading(-self.heading())
            self.forward(12)
            zombies.append(zombies())
        return zombies

# this for prize move function to keep it constantly moving
# deltax=random.randint(-2,2)
# deltay=random.randint(-2,2)
# self.goto(self.xcor()+deltax, self.ycor()+deltay)

class Bullet(Turtle):
    def __init__(self, player):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.color(player.color)
        self.setheading(player.heading())
        self.penup()
        self.goto(player.xcor(), player.ycor())
        self.st()

class Prize(Turtle):
  def __init__(self):
    super().__init__()
    self.ht()
    self.speed(0)
    self.color("red")
    self.shape("circle")
    self.penup()
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    self.goto(x,y)
    self.setheading(90)
    self.st()
    deltax=random.randint(-2,2)
    deltay=random.randint(-2,2)
    self.goto(self.xcor()+deltax, self.ycor()+deltay)
'''
Bullet() Class
Constructor ( def __init__(self) ):
- Input: player object
- Attributes:
	- Position: same as player
	- Heading: same as player
	- Player: the player
 
move(self):
- move 15 or more pixels forward
- should call on the die() method when the bullet leaves the playing area

die()
- hides the object. 
- removes object from the player's bullet list
'''
def die(self):
    self.alive =False
    self.ht()

#### DRIVER CODE ####

def update():
    if p1.distance(prize) <20 or p2.distance(prize)<20:
        prize.goto(random.randint(-200, 200), random.randint(-200,200))
        prize.move(0)
    p1.move()
    p2.move()
    for bullet in p1.bullets:
        bullet.move()
        if bullet.distance(zombies)<20:
            bullet.hideturtle()
            p1.bullets.remove(bullet)
            zombie.die()
            zombie.ht()
    for bullet in p2.bullets:
        bullet.move()
        if bullet.distance(zombies)<20:
            bullet.hideturtle()
            p2.bullets.remove(bullet)
            zombie.die()
            zombie.ht()
    for zombie in zombies:
        zombie.move()
        zombies.setheading(zombies.towards(p1,p2))
        if zombie.distance(p1)<20:
            p1.die()
            p1.ht()
        if zombie.distance(p2)<20:
            p2.die()
            p2.ht()

    screen.ontimer(update, 120)

# while loop info does it need to be in update function or still in its own while loop

screen = Screen()
screen.bgcolor("black")
screen.listen()
playing_area()

prize=Prize()
p1 = Player(100,0,"blue",screen,"Right","Left", "Up")
p2 = Player(-100,0,"red",screen,"d","a", "w")
zombies =[]
update()
# while p1.alive and p2.alive:
    # p1.move()
    # p2.move()
    # for bullet in p1.bullets:
    #     bullet.move()
    #     if bullet.distance(zombies)<20:
    #         bullet.hideturtle()
    #         p1.bullets.remove(bullet)
    #         zombie.die()
    #         zombie.ht()
    # for bullet in p2.bullets:
    #     bullet.move()
    #     if bullet.distance(zombies)<20:
    #         bullet.hideturtle()
    #         p2.bullets.remove(bullet)
    #         zombie.die()
    #         zombie.ht()
    # for zombies in Zombie:
    #     zombies.setheading(zombies.towards(p1,p2))
    # if zombies.distance(p1)<20:
    #     p1.die()
    #     p1.ht()
    # if zombies.distance(p2)<20:
    #     p2.die()
    #     p2.ht()


screen.mainloop()