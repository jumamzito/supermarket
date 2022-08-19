import random
# Zaibu Juma Wafula
# 150678
# Used stack overflow to find a better strategy for the computer moves as the one I had was very slow
# The rest of the work is purely my own work


''' initialize the required lists as global variables'''
main_pile=[]
discard_pile=[]
computer_tower=[]
human_tower=[]
human_tower2=[]

def main():
    ''' main function where the game starts'''
    global main_pile,discard_pile,computer_tower,human_tower,human_tower2
    instructions()
    setup_bricks()

    #transfer the bricks to the main pile and discard pile
    results = setup_bricks()
    main_pile = results[0]
    discard_pile = results[1]

    shuffle_bricks(main_pile)
    deal=deal_initial_bricks(main_pile)

   

    initial_discard = main_pile.pop(0)
    discard_pile.append(initial_discard)

    #Call the player selection function to decide who to play with
    player_reponse = player_selection()
    if player_reponse == 1:
        computer_tower = deal[0]
        human_tower = deal[1]
        human_vs_comp()

    elif player_reponse == 2:
        human_tower2 = deal[0]
        human_tower = deal[1]
        human_vs_human()


# Set up the intial set up bricks to initialize the main pile and discard pile
def setup_bricks():
    '''Function to initialize 60 bricks'''
    main_pile=[*range(1, 61, 1)]
    discard_pile=[]
    set=(main_pile,discard_pile)
    return set


# print(setup_bricks())

# shuffle the bricks using random shuffle
def shuffle_bricks (bricks):
    '''Function to shuffle the bricks before dealing to the players'''
    random.shuffle(bricks)

# Check if the main pile is empty and transfer the discard pile to it.
def check_bricks(main_pile, discard):
    '''Function to check if the main pile has bricks and if empty shuffle and tranfer the discard pile bricks to the main pile'''
    if len(main_pile):
            
        print("main pile still has blocks")
    else:
        random.shuffle(discard)
        main_pile = discard
        discard=[]
        popped=main_pile.pop(0)
        discard.append(popped)

# Check if the tower is sorted.
def check_tower_blaster(tower):
    '''Check if the tower has been sorted '''
    flag = 0
    if(tower == sorted(tower)):
        flag = 1
        
    # returning the true or false if the flag option is 1 or zero
    if (flag) :
        return True
    else :
        return False


def get_top_brick(brick_pile):
    '''Function to get the top brick'''
    top_brick=brick_pile.pop(0)
    return top_brick

def deal_initial_bricks(main_pile):
    '''Function to deal bricks to the players'''
    computer=[]
    user=[]
    while len(computer)<10 and len(user)<10:
        try:
            value1=main_pile.pop(0)
            computer.append(value1)
            value2=main_pile.pop(0)
            user.append(value2)
        except IndexError:
            break
            
    return computer,user


def add_brick_to_discard(disc_value, discard_pile):
    '''Function to add brick to discard pile'''
    discard_pile.insert(0, disc_value)


def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
    '''Function to find and replace a brick from a given tower'''
    if brick_to_be_replaced in tower:
        index_name=tower.index(brick_to_be_replaced)
        tower.remove(brick_to_be_replaced)
        tower.insert(index_name,new_brick)
        discard.append(brick_to_be_replaced)

        return True
    else:

        return False


def computer_play(computer_tower, main_pile, discard_pile):
    """
    This function is the computer's strategy of replacing bricks.
    Given the computer's tower and top discard brick, determine whether this brick is useful,
    then determine which brick to take, and which index position to place brick.
    """
    discard_top = discard_pile[0]

    # The computer's strategy is to 'slice' the pile of 60 bricks into 10 groups (divide by 6),
    # and based on each block's value, distribute them across 10 slots in the computer's tower.
    #
    # The computer wants to intentionally fill the beginning and end of the tower first,
    # if the top brick on the discard pile is less than 19 or more than 42, take it.
    # Take that brick's number (minus 1, as indexes start at 0) and divide it by 6,
    # that will be the index position for the brick.
    #
    # In other words, if the top discard brick is:
    # 1 ~ 6, place in 1st block position (index 0)
    # 7 ~ 12, place in 2nd block position (index 1)
    # 13 ~ 18, place in 3rd block position (index 2)
    # 19 ~ 42, don't take it. Take brick from main pile. (See strategy below)
    # 43 ~ 48, place in 8th block position (index 7)
    # 49 ~ 54, place in 9th block position (index 8)
    # 55 ~ 60, place in 10th block position (index 9)

    if discard_top < 19 or discard_top > 42:
        computer_tower_index = (discard_top - 1) // 6
        brick_to_remove = computer_tower[computer_tower_index]
        computer_tower[computer_tower_index] = discard_top  # Place new brick and move unwanted brick into discard.
        # discard_pile[0] = brick_to_remove
        add_brick_to_discard(brick_to_remove, discard_pile)
        print(f"The computer picked {computer_tower[computer_tower_index]} from the discard pile.")
        #print(f'comp tower {computer_tower}') # checking the comp pile is working
        return computer_tower

    # If the top brick on the discard pile is between 19 and 42, then take a brick from main pile.
    # This brick (minus 1, as indexes start at 0), divided by 6, will be the index position to place it.
    #
    # If the revealed brick from main brick is:
    # 1 ~ 6, place in 1st block position (index 0)
    # 7 ~ 12, place in 2nd block position (index 1)
    # 13 ~ 18, place in 3rd block position (index 2)
    # 19 ~ 24, place in 4th block position (index 3)
    # 25 ~ 30, place in 5th block position (index 4)
    # 31 ~ 36, place in 6th block position (index 5)
    # 37 ~ 42, place in 7th block position (index 6)
    # 43 ~ 48, place in 8th block position (index 7)
    # 49 ~ 54, place in 9th block position (index 8)
    # 55 ~ 60, place in 10th block position (index 9)
    # The computer's strategy does not discard a brick from main pile.

    if 18 < discard_top < 43:
        taken_from_main = get_top_brick(main_pile) # Pick top brick of the main pile
        computer_tower_index = (taken_from_main - 1) // 6
        brick_to_remove = computer_tower[computer_tower_index]
        computer_tower[computer_tower_index] = taken_from_main
        discard_pile.insert(0, brick_to_remove)
        add_brick_to_discard(brick_to_remove, discard_pile)  # Place new brick and move unwanted brick into discard.
        print(f"The computer picked {computer_tower[computer_tower_index]} from the main pile.")
        # print(f'comp tower {computer_tower}') # Checking comp tower is updating
        return computer_tower


def human_play(human_tower, main_pile, discard_pile):
    '''Function to play the human moves'''
    print(f'Current tower is: {human_tower}')
    print(f'Current top value on discard is: {discard_pile[0]}')

    request_area=input('Do you want to pick main pile or discard pile? M=main,D=discard: ') # Check which pile to choose from
    if (request_area.startswith('D') or request_area.startswith('d')) and request_area !="": # Check if the value entered is d or starts with d
        new_brick=discard_pile.pop(0)
        brick_to_be_replaced=int(input('Enter a value to be replaced in the tower: ')) # Value to be replaced is requested

        find_and_replace(new_brick, brick_to_be_replaced, human_tower, discard_pile) # Function to find replace the requested value is called

    elif (request_area.startswith('M') or request_area.startswith('m')) and request_area !="": # Check if the value entered is m or starts with m
        print(f'Current top value on discard is: {main_pile[0]}')
        new_brick=main_pile.pop(0)
        brick_to_be_replaced=int(input('Enter a value to be replaced in the tower: '))
        find_and_replace(new_brick, brick_to_be_replaced, human_tower, discard_pile) # Function to find replace the requested value is called

    else:
        print('Enter the correct value')
        human_play(human_tower, main_pile, discard_pile) # user is returned to the start of the function to enter the correct value

    
    check_tower_blaster(human_tower)

    return human_tower


def player_selection():
    '''Function to check which version of the game to be played with computer or with a friend'''
    
    try:
        response = int(input('Enter 1 to play against Computer 2 to play against a human: '))
        if response == 1:
            print('comp vs human')

            # human vs comp
            return response
        elif response == 2:
            print('human vs human')
            # play against human
            return response
        
        else:
            print('Enter either 1 or two as per the instructions')
            player_selection()
    except:
        print('The field only takes integers')
        player_selection()

    
# Human vs computer part of the game 
def human_vs_comp():
    '''Function that is called to start the game between human and computer'''
    while True:
            # computer starts the game by calling the computer play function
        computer_play(computer_tower, main_pile, discard_pile) 
        comp_response=check_tower_blaster(computer_tower) #check if computer won the game
        if comp_response:
            print('Computer wins the game')
            break
        
        else:
            print('Game on')
        check_bricks(main_pile, discard_pile)
        human_play(human_tower, main_pile, discard_pile) #Human function called to play their turn
        hum_response=check_tower_blaster(human_tower) #check if human won the game
        if hum_response:
            print('You won the game')
            break
        
        else:
            print('Game on')
        check_bricks(main_pile, discard_pile)
# Human vs human part of the game is called here
def human_vs_human():
    '''Human vs human part of the game'''
    while True:
        # Call the human moves function for player 1 
        print('Player one')
        human_play(human_tower, main_pile, discard_pile)
        hum_response=check_tower_blaster(human_tower) #check if player one won the game
        if hum_response:
            print('You won the game')
            break
        
        else:
            print('Game on')
            print('Player two next')
        check_bricks(main_pile, discard_pile) 
        # Call the human moves function for player 2 
        print('Player Two')
        human_play(human_tower2, main_pile, discard_pile)
        hum_response=check_tower_blaster(human_tower2) #check if player two won the game
        if hum_response:
            print('You won the game')
            break
        
        else:
            print('Game on')
            print('Player one next')
        check_bricks(main_pile, discard_pile)

def instructions():
    '''Tells the user the rules of the game.'''
    print ('"Tower blaster is a game that can be played with two people or with a computer\n'
          'this version of the game will enable the person who starts the game to either choose to play with the computer or with a friend \n'
          'The computer part of the game is very simple but for better experience play with a friend \n'
          'Let\'s start! \n'
          '  \n'
          '****** \n'
          '  ')

if __name__ == '__main__':
    main()  