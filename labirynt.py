import sys, tty, termios, os

board = board = [
    ['∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','╔','═','═','╗','╔','═','═','╗','∙','╔','═','═','═','═','═','╗','∙','╔','═','═','╗','∙','∙','∙','∙','∙','∙','∙','╔','═','═','═','╗','∙','∙'],
    ['∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','╔','╝','░','░','║','║','░','░','║','∙','║','░','░','░','░','░','║','∙','║','░','░','║','∙','∙','∙','∙','∙','∙','╔','╝','░','░','░','╚','╗','∙'],
    ['∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','║','░','░','░','║','║','░','░','║','∙','║','░','░','░','░','░','║','∙','║','░','░','╚','═','╗','∙','∙','∙','∙','║','░','░','░','░','░','╚','═'],
    ['∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','║','░','░','╔','╝','║','░','░','║','∙','║','░','░','╔','═','═','╝','∙','║','░','░','░','░','║','∙','∙','╔','═','╝','░','░','╥','░','░','░','E'],
    ['∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','║','░','░','║','╔','╝','░','░','╚','═','╝','░','░','╚','═','╗','∙','∙','║','░','░','░','░','║','∙','∙','║','░','░','░','░','║','░','░','░','E'],
    ['∙','∙','╔','═','═','╗','∙','∙','╔','═','═','═','╝','░','░','║','║','░','░','░','░','░','░','░','░','░','░','╚','═','═','╩','═','╡','░','░','╚','═','═','╣','░','░','╔','═','╩','═','═','═','═'],
    ['∙','∙','║','░','░','╚','╗','∙','║','░','░','░','░','░','░','║','║','░','░','░','░','░','░','░','░','░','░','░','░','░','░','░','░','░','░','░','░','░','║','░','░','║','∙','∙','∙','∙','∙','∙'],
    ['∙','╔','╝','░','░','░','╚','═','╝','░','░','░','░','░','░','║','╚','═','═','╗','░','░','╔','═','═','╗','░','░','░','░','░','░','░','░','░','░','░','░','║','░','░','║','∙','∙','∙','∙','∙','∙'],
    ['╔','╝','░','░','╥','░','░','░','░','░','░','╔','═','═','═','╝','∙','∙','∙','║','░','░','║','∙','∙','║','░','░','░','╔','═','═','═','═','═','╗','░','░','╨','░','░','╚','═','═','═','╗','∙','∙'], 
    ['║','░','░','░','╠','╗','░','░','░','░','╔','╝','∙','∙','∙','∙','∙','∙','∙','║','░','░','╚','╗','∙','╚','╗','░','░','╚','═','═','╗','∙','∙','║','░','░','░','░','░','░','░','░','░','║','∙','∙'],
    ['║','░','░','░','║','║','░','░','░','░','║','∙','∙','∙','∙','╔','═','═','╗','║','░','░','░','║','∙','∙','║','░','░','░','░','░','╚','═','╗','║','░','░','░','░','░','░','░','░','░','║','∙','∙'],
    ['╚','═','═','╦','╝','╚','╡','░','░','╠','╣','∙','╔','═','═','╝','░','░','╚','╝','░','░','░','╚','═','═','╣','░','░','░','░','░','░','░','║','║','░','░','╔','═','═','╗','░','░','╔','╝','∙','∙'],
    ['∙','∙','∙','║','░','░','░','░','░','░','║','∙','║','░','░','░','░','░','░','░','░','░','░','░','░','░','╠','═','═','╗','░','░','░','░','║','║','░','░','║','∙','∙','║','░','░','║','∙','∙','∙'],
    ['╔','═','═','╬','╗','░','░','░','░','░','╠','═','╝','░','░','░','░','░','░','░','░','░','░','░','░','░','║','∙','∙','╚','═','╗','░','░','║','║','░','░','╚','╗','∙','║','░','░','╚','╗','∙','∙'],
    ['║','░','░','╚','╝','░','░','░','░','░','╨','░','░','░','░','╔','═','═','═','╗','░','░','╔','╗','░','░','║','∙','∙','∙','∙','║','░','░','║','║','░','░','░','║','∙','║','░','░','░','║','∙','∙'],
    ['║','░','░','░','░','░','╥','░','░','░','░','░','░','░','░','╚','═','═','═','╣','░','░','║','║','░','░','╚','═','═','╗','∙','║','░','░','║','║','░','░','░','║','∙','╚','╗','░','░','║','∙','∙'],
    ['║','░','░','░','░','░','║','░','░','░','░','░','╥','░','░','░','░','░','░','║','░','░','║','║','░','░','░','░','░','║','∙','╚','═','═','╝','╚','═','═','═','╝','∙','∙','║','░','░','║','∙','∙'],
    ['║','░','░','░','╔','═','╩','═','═','═','═','═','╣','░','░','╔','╗','░','░','║','░','░','║','║','░','░','░','░','░','║','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','╚','═','═','╝','∙','∙'],
    ['╚','═','═','═','╝','∙','∙','∙','∙','∙','∙','∙','║','░','░','║','║','░','░','╠','═','═','╝','╚','═','═','═','═','═','╝','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙'],
    ['∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','║','░','░','║','║','╞','═','╝','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙'],
    ['∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙','∙'] 
    ]

hero_y = 19
hero_x = 13

# TODO Draw board function
def drawBoard():
    y=0
    for row in board:
        x = 0
        for field in row:
            if x == hero_x and y == hero_y:
                    print(hero, end= '')
            else:
                    print(field, end = '')
            x+=1
        print()
        y+=1
    do_health()

def nameHero():
    while True:
        hero_name = input("Witaj w grze LabirynyRPG, nazwij swojego Wiedźmaka jednym znakiem: ")
        if len(hero_name) == 1: 
            break
        else:
            print("Jednym znakiem:)")
    return hero_name

hero = nameHero()

def startGame():
    while True:
        print('Wpisz start żeby zacząć')
        button_start = input()
        if button_start == 'start' or button_start == 'START' or button_start == 'Start':
            drawBoard()
            break
        else:
            print('Przestań szukać błędów w kodzie')

def do_health():
    health = 200.0     # Current Health (float so division doesn't make an int)
    maxHealth = 200    # Max Health
    healthDashes = 20  # Max Displayed dashes

    dashConvert = int(maxHealth/healthDashes)            # Get the number to divide by to convert health to dashes (being 10)
    currentDashes = int(health/dashConvert)              # Convert health to dash count: 200/10 => 20 dashes
    remainingHealth = healthDashes - currentDashes       # Get the health remaining to fill as space => 12 spaces
    healthDisplay = '-' * currentDashes                  # Convert 8 to 8 dashes as a string:   "--------"
    remainingDisplay = ' ' * remainingHealth             # Convert 12 to 12 spaces as a string: "            "
    percent = str(int((health/maxHealth)*100)) + "%"     # Get the percent as a whole number:   100%

    print("|" + healthDisplay + remainingDisplay + "|")  # Print out textbased healthbar
    print("   HERO HEALTH " + percent)                   # Print the percent

def funcWin():
    os.system('clear')
    print('ZWYCIĘSTWOOOO')
    #startGame()

def functPowrot():
    os.system('clear')
    print('Wyjście jest w drugą stronę')
    startGame()

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def wallDetection():
    
    print("Głową muru nie przebijesz, idź ścieżka")
    
def movement():
    global hero_y, hero_x
    checking_character = getch()
    while True: 
        # Move up - collision, movement,(y-1)
        if(checking_character == 'w' or checking_character == 'W'):
            # Check position
            if board[hero_y-1][hero_x] == '░':
                hero_y-=1
                os.system('clear')
                drawBoard()
            else:
                wallDetection()
        # Move down (y-1)
        if (checking_character == 's' or checking_character == 'S'):
            # Check position
            if board[hero_y+1][hero_x] == '░':
                hero_y+=1
                os.system('clear')
                drawBoard()
            elif board[hero_y+1][hero_x] == '∙':
                functPowrot()
            else:
                wallDetection()

        # Move left (x-1)
        if (checking_character == 'a' or checking_character == 'A'):
            # Check position
            if board[hero_y][hero_x-1] == '░':
                hero_x-=1
                os.system('clear')
                drawBoard()
            else:
                wallDetection()

        # Move right (x+1)
        if (checking_character == 'd' or checking_character == 'D'):
            if board[hero_y][hero_x+1] == '░':
                hero_x+=1
                os.system('clear')
                drawBoard()
            elif board[hero_y][hero_x+1] == 'E':
                funcWin()
            else:
                wallDetection()
        checking_character = getch()   

def main():
    startGame()
    movement()
    do_health()

main()

