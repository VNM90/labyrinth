import sys, tty, termios, os, random

hero_y = 19
hero_x = 13
health = 200.0
inv = {'silver sword': 1, 'steel sword': 1, 'orens': 42, 'diamond': 0, 'fisstech':20}
loot = ['diamond'] # ADDING TO FUNCTION ADDINVENTORY EVERY STEP INCREASE DIAMOND IN TABLE BECAUSE BOARD IS REFRESHED EVERY TIME

def game():

    board = [
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
        # addInventory(inv,loot) 
        printTable(inv)
        # displayInventory(inv)
        doHealth()

    def nameHero():
        while True:
            hero_name = input("Witaj w grze LabirynyRPG, zbierz wszystkie diamenty($) i udaj się do wyjścia(EXIT).\nNazwij swojego Wiedźmaka jednym znakiem: ")
            if len(hero_name) == 1: 
                break
            else:
                print("Jednym znakiem:)")
        return hero_name

    hero = nameHero()

    def diamonds():
        diamond = 0
        while diamond <= 4:  # I don't know why print 5 elements
            diamondX = random.randint(0,20) #randomize diamond position NEED TEST
            diamondY = random.randint(0,45) #randomize diamond position NEED TEST
            if board[diamondX][diamondY] == '░':
                board[diamondX][diamondY] = "$" #should be diamond symbol
            else:
                diamond -= 1
            diamond+=1

    def startGame():
        while True:
            print('Wpisz start żeby zacząć')
            button_start = input()
            if button_start == 'start' or button_start == 'START' or button_start == 'Start':
                drawBoard()
                break
            else:
                print('Przestań szukać błędów w kodzie')

    def restartGame():
        global health,hero_x,hero_y
        answer = input("Restart? Y/N ")
        if answer == "N" or answer == 'n':
            print ("Leaving the game")
            sys.exit(0) # import sys module 
        elif answer == "Y" or answer == 'y':
            print ("Starting new game")
            health = 200
            hero_y = 19
            hero_x = 13
            game() 
        else: 
            print ("Nie rozpoznano znaku: LEAVING THE GAME")
            sys.exit(0)

    def doHealth():
        global health   
        maxHealth = 200    # Max Health
        healthDashes = 20  # Max Displayed dashes

        dashConvert = int(maxHealth/healthDashes)            # Get the number to divide by to convert health to dashes (being 10)
        currentDashes = int(health/dashConvert)              # Convert health to dash count: 200/10 => 20 dashes
        remainingHealth = healthDashes - currentDashes       # Get the health remaining to fill as space => 12 spaces
        healthDisplay = '-' * currentDashes                  # Convert dashes as a string:   "--------"
        remainingDisplay = ' ' * remainingHealth             # Convert  spaces as a string: "            "
        percent = str(int((health/maxHealth)*100)) + "%"     # Get the percent as a whole number:   100%
    
        print("|" + healthDisplay + remainingDisplay + "|")  # Print out textbased healthbar
        print("   HERO HEALTH " + percent)                   # Print the percent

    def funcWin():
        os.system('clear')
        print('STAGE CLEAR')
        restartGame()

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
        global health,hero_x,hero_y
        health -= 20
        print("Palisz się tracisz 10% punktów zdrowia")
        if health == 0:
            os.system('clear')
            print("YOU DIED")
            restartGame()
       
    def movement():
        global hero_y, hero_x
        checking_character = getch()
        while True:  
            if(checking_character == 'w' or checking_character == 'W'): # Move up - collision, movement,(y-1)
                if board[hero_y-1][hero_x] == '░':  # Check position
                    hero_y-=1
                    os.system('clear')
                    drawBoard()
                else:
                    wallDetection()
            
            if (checking_character == 's' or checking_character == 'S'): # Move down (y-1)
                if board[hero_y+1][hero_x] == '░':  # Check position
                    hero_y+=1
                    os.system('clear')
                    drawBoard()
                elif board[hero_y+1][hero_x] == '∙':
                    functPowrot()
                else:
                    wallDetection()

            if (checking_character == 'a' or checking_character == 'A'): # Move left (x-1)
                if board[hero_y][hero_x-1] == '░':  # Check position
                    hero_x-=1
                    os.system('clear')
                    drawBoard()
                else:
                    wallDetection()

            if (checking_character == 'd' or checking_character == 'D'): # Move right (x+1)
                if board[hero_y][hero_x+1] == '░':  # Check position
                    hero_x+=1
                    os.system('clear')
                    drawBoard()
                elif board[hero_y][hero_x+1] == 'E':
                    funcWin()
                else:
                    wallDetection()
            checking_character = getch()   

    def displayInventory(inventory):
        for i, count in inventory.items():
            print(i,count)

    def addInventory(inventory, added_items):
        for i in added_items:
            if i in inventory:
                inventory[i]+=1
            else:
                inventory[i]=1

    def printTable(inventory, order=None):
        itemName = "item name"
        countName = 'count'

        maxWidthItem = max([len(str(i)) for i in inventory.keys()] + [len(itemName)])
        maxWidthCount = max([len(str(count)) for count in inventory.values()] + [len(countName)])

        #header
        print('-' * (maxWidthItem + maxWidthCount + 3))
        print(f"{itemName:>{maxWidthItem}} | {countName:>{maxWidthCount}}")
        print('-' * (maxWidthItem + maxWidthCount + 3))

        #rows
        for i, count in inventory.items():
            print(f"{i:>{maxWidthItem}} | {count:>{maxWidthCount}}")

        #footer
        print('-' * (maxWidthItem + maxWidthCount + 3))

    def main():
        diamonds()
        startGame()
        movement()

    main()

game()
