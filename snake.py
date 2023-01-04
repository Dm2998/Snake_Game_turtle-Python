import turtle
import random


# Set the turtle's speed and shape. You can also set the turtle's color and pen size if desired.
# Define the directions for the snake. For example, you can use variables like up, down, left, and right to represent the directions the snake can move in.
# Set the starting position and direction for the snake. You can use a list to store the positions of the snake and a variable to store the direction it is moving in.
# Create a function to draw the snake. This function should use the turtle's goto and setheading methods to move the turtle to the positions of the snake and draw lines between them.
# Create a function to draw the food. This function should use the turtle's goto and dot methods to move the turtle to the position of the food and draw a dot there.
# Create a function to move the snake. This function should update the position of the snake based on its direction. It should also check if the snake has hit a wall or itself, and end the game if it has.
# Create a function to check if the snake has eaten the food. If it has, the function should increase the length of the snake and generate a new position for the food.
# Set the key bindings for the snake. You can use the turtle's onkey method to bind specific keys to specific functions that change the direction of the snake.
# Create the game loop. In the loop, you should draw the snake and the food, move the snake, and check if the snake has eaten the food. You can use the turtle's update method to update the screen after each iteration of the loop



# Set the turtle's speed
turtle.speed('fastest')

# Set the turtle's shape
turtle.shape('square')

# Set the turtle's color
turtle.color('black', 'green')  

# Set the turtle's pen size
turtle.pensize(3)

turtle.bgcolor('blue')


# Set the game variables
snake_speed = 10
snake_length = 1
snake_positions = []
food_position = (0, 0)
score = 0


# Set the directions for the snake
up = (0, snake_speed)
down = (0, -snake_speed)
left = (-snake_speed, 0)
right = (snake_speed, 0)


# Set the starting position and direction for the snake
snake_positions = [(0, 0)]
snake_direction = right
snake = turtle.clone()
snake.hideturtle()

# Create a function to draw the snake
def draw_snake():
    position = snake_positions[0]
    new_x = position[0] + snake_direction[0]
    new_y = position[1] + snake_direction[1]
    new_position = (new_x, new_y)
    snake_positions.insert(0, new_position)
    snake_positions.pop()
    snake.goto(new_position)
    snake.stamp()
    turtle.ontimer(draw_snake, 100)
    turtle.update()
    turtle.mainloop()

# Create a function to draw the food
food = turtle.clone()
food.penup()
food.hideturtle()
food.goto(100, 100)
food.dot(10, 'red')
#Create a function to move the snake
def move_snake():
    new_x = snake_positions[0][0] + snake_direction[0]
    new_y = snake_positions[0][1] + snake_direction[1]
    new_position = (new_x, new_y)
    snake_positions.insert(0, new_position)
    snake_positions.pop()
    draw_snake()

#Create a function to change the snake's direction
def up_snake():
    if snake_direction != down:
        snake_direction = up

#Create a function to the snake down

def down_snake():
    if snake_direction != up:
        snake_direction = down
        return food_position
#Create a function to snake left
def left_snake():
    if snake_direction != right:
        snake_direction = left
        return food_position

#Create a function to snake right

def right_snake():
    if snake_direction != left:
        snake_direction = right
        return food_position
#Create a function to move the snake with the keyboard 

def move_teclado():
    turtle.onkey(up_snake, 'Up')
    turtle.onkey(down_snake, 'Down')
    turtle.onkey(left_snake, 'Left')
    turtle.onkey(right_snake, 'Right')


# Create a function to check if the snake has eaten the food
def check_food():
    if snake_positions[0] == food.position():
        food_x = random.randint(-200, 200)  # Generate a random x position for the food
        food_y = random.randint(-200, 200)
        food.goto(food_x, food_y)
        new_x = snake_positions[0][0] + snake_direction[0]
        new_y = snake_positions[0][1] + snake_direction[1]
        new_position = (new_x, new_y)
        snake_positions.insert(0, new_position)
        draw_snake()
    elif snake_positions[0][0] > 200 or snake_positions[0][0] < -200 or snake_positions[0][1] > 200 or snake_positions[0][1] < -200:
        food_x = random.randint(-200, 200)  # Generate a random x position for the food
        food_y = random.randint(-200, 200)
        right_snake()
        left_snake()
        up_snake()
        down_snake()
        print('You hit the wall!')
        quit()
    elif snake_positions[0] in snake_positions[1:]:
        food_x = random.randint(-200, 200)
        food_y = random.randint(-200, 200)
        right_snake()
        left_snake()
        up_snake()
        down_snake()
        print('You hit yourself!')
        quit()

turtle.listen()

# Create the game loop
while True:  # Run the game forever
    move_snake()
    check_food()
    up_snake()
    down_snake()
    left_snake()
    right_snake()
    turtle.update()
    turtle.ontimer(move_snake, 100)
    turtle.ontimer(check_food, 100)
    turtle.update()
    turtle.mainloop()

# Run the game
turtle.mainloop()


