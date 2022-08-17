from ast import Return
import random

# global main_pile

# global discard

main_pile=[]
discard_pile=[]
computer_tower=[]

def main():
    setup_bricks()

    results = setup_bricks()
    main_pile = results[0]
    discard_pile = results[1]

    shuffle_bricks(main_pile)
    deal=deal_initial_bricks(main_pile)
    computer_tower = deal[0]
    human_tower = deal[1]

    initial_discard = main_pile.pop(0)
    discard_pile.append(initial_discard)

    computer_play(computer_tower, main_pile, discard_pile)
    human_play(human_tower, main_pile, discard_pile)
    
    
    
    
    check_bricks(main_pile, discard_pile)








# Set up the intial set up bricks to initialize the main pile and discard pile
def setup_bricks():
    main_pile=[*range(1, 61, 1)]
    discard_pile=[]
    set=(main_pile,discard_pile)
    return set


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


def add_brick_to_discard(disc_value, discard_pile):
    discard_pile.append(disc_value)


def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
    if brick_to_be_replaced in tower:
        index_name=tower.index(brick_to_be_replaced)
        tower.remove(brick_to_be_replaced)
        tower.insert(index_name,new_brick)
        discard.append(brick_to_be_replaced)

        return True
    else:

        return False


def computer_play(computer_tower, main_pile, discard_pile):
    
    if computer_tower[0]>discard_pile[0]:
        value=discard_pile.pop(0)
        disc_value=computer_tower.pop(0)
        computer_tower.append(value)
        add_brick_to_discard(disc_value, discard_pile)
        # discard_pile.append(disc_value)

    elif computer_tower[-1]<discard_pile[0]:
        value=discard_pile.pop(0)
        disc_value=computer_tower.pop(-1)
        computer_tower.insert(-1,value)
        add_brick_to_discard(disc_value, discard_pile)
        # discard_pile.append(disc_value)
    
    else:
        value=main_pile.pop(0)
        if value<computer_tower[0]:
            disc_value=computer_tower.pop(0)
            computer_tower.append(value)
            add_brick_to_discard(disc_value, discard_pile)
            # discard_pile.append(disc_value)

        elif value>computer_tower[-1]:
            disc_value=computer_tower.pop(-1)
            computer_tower.insert(-1,value)
            add_brick_to_discard(disc_value, discard_pile)
            # discard_pile.append(disc_value)

    check_tower_blaster(computer_tower)
    

    return computer_tower



def human_play(human_tower, main_pile, discard_pile):
    print(f'Current tower is: {human_tower}')
    print(f'Current top value on discard is: {discard_pile[0]}')

    request_area=input('Do you want to pick main pile or discard pile? M=main,D=discard: ')
    if request_area == 'D':
        new_brick=discard_pile.pop(0)
        brick_to_be_replaced=input('Enter a value to be replaced in the tower: ')

        find_and_replace(new_brick, brick_to_be_replaced, human_tower, discard_pile)

    elif request_area == 'M':
        new_brick=main_pile.pop(0)
        brick_to_be_replaced=input('Enter a value to be replaced in the tower: ')
        find_and_replace(new_brick, brick_to_be_replaced, human_tower, discard_pile)

    else:
        request_area=input('Do you want to pick main pile or discard pile? M=main,D=discard: ')

    
    check_tower_blaster(human_tower)

    return human_tower


if __name__ == '__main__':
    main()   