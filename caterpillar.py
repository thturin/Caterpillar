import random
import turtle as t


def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180: #check if head is pointing to the right (0) or left (180)
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_right():
    if caterpillar.heading()==90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)

def move_left():
    if caterpillar.heading()==90 or caterpillar.heading()==270:
        caterpillar.setheading(180)

def outside_window(): #this function can be done by students. leave the pass variables
    #create vars
    window_l = -t.window_width()/2
    window_r = t.window_width()/2
    window_t = t.window_height()/2
    window_b = -t.window_height()/2
    (x,y) = caterpillar.pos() #get the caterpillar position
    outside = x<window_l or x>window_r or y>window_t or y<window_b #returns a boolean of true if any of these inequalities are true
    return outside

def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER', align='center',font=('Arial',30,'normal'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width()/2)-50
    y = (t.window_height()/2)-50
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score), align='right', font=('Arial',40,'bold'))

def place_leaf(): #get moving
    leaf.ht() #same as hideturtle()
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    leaf.setpos(x,y)
    leaf.st() #showturtle()


def start_game(): #initiate the game
    global game_started #variable is read by all functions in program
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()

    caterpillar_speed = 2
    caterpillar_length = 1
    caterpillar.shapesize(1,caterpillar_length,1) #turtle stretches into shape size
    caterpillar.showturtle()
    display_score(score) #DISPLAY the score
    place_leaf() #call
    while True:
        caterpillar.forward(caterpillar_speed) #move forward
        # the catepillar eats the leaf once its 20 pixels away
        if caterpillar.distance(leaf) < 20:  # returns distance from turtle to arg (leaf)
            place_leaf()  # replenish the leaf because its been eaten
            caterpillar_length += 1
            caterpillar.shapesize(1, caterpillar_length, 1)  # stretch_width, stretch_length -> makes the caterpillar longer after eating leaf
            caterpillar_speed += 1 #caterpillar goes faster
            score += 10 #add to score
            display_score(score) # display the new score
        if outside_window():
            game_over()
            break



t.bgcolor('yellow')

#create the caterpillar turtle
caterpillar = t.Turtle() #create a new caterpillar as a turtle object
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(1)
caterpillar.penup()
caterpillar.hideturtle()


#create a leaf turtle
leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf',leaf_shape) #basically creating your own custom shape that the leaf object will register and use instances of
leaf.shape('leaf')  #now you cna use the leaf shape here
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)


game_started = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start ', align='center', font=('Arial',16,'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

t.onkey(start_game, 'space') #call start_game function when key space bar is pressed
t.onkey(move_up,'Up')
t.onkey(move_down,'Down')
t.onkey(move_right,'Right')
t.onkey(move_left,'Left')
t.listen() #progrma listens for event
t.mainloop() #loop the program infinitely
