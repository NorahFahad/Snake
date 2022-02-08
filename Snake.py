#import library
import random
import curses

s = curses.initscr() #initialize screen (.initscr() returns a window object representing the entire screen)
curses.curs_set(0) #0 means false to set the cursor invisible
sh, sw = s.getmaxyx() #sh the hight, sw the width of the screen 
w = curses.newwin(sh, sw, 0, 0) #w is new window
w.keypad(1) #tell the window to recive keypad
w.timeout(100) #refresh to the screen

#snake first position
snk_x = sw//4  
snk_y = sh//2

snake = [
    [snk_y, snk_x], #snake head
    [snk_y, snk_x-1], #snake body
    [snk_y, snk_x-2] #snake body
]

food = [sh//2, sw//2] #food first position
w.addch(food[0], food[1], curses.ACS_PI) #charectar food show in screen

key = curses.KEY_RIGHT #store the key pressed #the snake first go right

while True:
    next_key = w.getch() #next key pressed
    key = key if next_key == -1 else next_key

    #condition if the snake hit the limits of the window or himself, GAMEOVER
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1: ]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    #movement of the snake
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    
    snake.insert(0, new_head) #the new head after movement

    if snake[0] == food: #if the head of the snake eat the food
        food = None #take of the food
        while food is None: #new food in the screen
            nf = [ #list new food random in the screen
                random.randint(1, sh-1), #between 1 and the end of the hight of screen -1
                random.randint(1, sw-1) #between 1 and the end of the width of screen -1
            ]
            food = nf if nf not in snake else None #if the new random food is not in the body of the snake
        w.addch(food[0], food[1], curses.ACS_PI) #show the new food in the screen

    else:
        tail = snake.pop() #pop the tail if the snake doesnot eat food
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD) #show the body of the snake
