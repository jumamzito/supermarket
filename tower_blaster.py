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


