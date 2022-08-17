from ast import Return
import random

# Set up the intial set up bricks to initialize the main pile and discard pile
def setup_bricks():
    main_pile=[*range(1, 61, 1)]
    discard_pile=[]

    return main_pile,discard_pile


# print(setup_bricks())

# shuffle the bricks using random shuffle
def shuffle_bricks (bricks):
    random.shuffle(bricks)

# Check if the main pile is empty and transfer the discard pile to it.
def check_bricks(main_pile, discard):
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
    flag = 0
    if(tower == sorted(tower)):
        flag = 1
        
    # returning the true or false if the flag option is 1 or zero
    if (flag) :
        return True
    else :
        return False


def get_top_brick(brick_pile):
    top_brick=brick_pile.pop(0)
    return top_brick

def deal_initial_bricks(main_pile):
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


def add_brick_to_discard(brick, discard):
    discard.append(brick)


def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
    if brick_to_be_replaced in tower:
        index_name=tower.index(brick_to_be_replaced)
        tower.remove(brick_to_be_replaced)
        tower.insert(index_name,new_brick)
        discard.append(brick_to_be_replaced)

        return True
    else:

        return False


def computer_play(tower, main_pile, discard):
    
    if tower[0]>discard[0]:
        value=discard.pop(0)
        disc_value=tower.pop(0)
        tower.append(value)
        discard.append(disc_value)

    elif tower[-1]<discard[0]:
        value=discard.pop(0)
        disc_value=tower.pop(-1)
        tower.insert(-1,value)
        discard.append(disc_value)
    
    else:
        value=main_pile.pop(0)
        if value<tower[0]:
            disc_value=tower.pop(0)
            tower.append(value)
            discard.append(disc_value)

        elif value>tower[-1]:
            disc_value=tower.pop(-1)
            tower.insert(-1,value)
            discard.append(disc_value)

    return tower



            




        
