# def ask_yes_or_no(prompt):
#     prompt = input('Do You want to play the Game (Y/N):  ')
#     if (prompt.startswith('Y') or prompt.startswith('y')) and prompt !="":
        
#         return True
        
#     elif (prompt.startswith('N') or prompt.startswith('n')) and prompt !="":
#         return False

#     else:
#         ask_yes_or_no(prompt)


def computer_play(tower, main_pile, discard):
    """
    This function is the computer's strategy of replacing bricks.
    Given the computer's tower and top discard brick, determine whether this brick is useful,
    then determine which brick to take, and which index position to place brick.
    """
    discard_top = discard[0]

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
        brick_to_remove = tower[computer_tower_index]
        tower[computer_tower_index] = discard_top  # Place new brick and move unwanted brick into discard.
        discard[0] = brick_to_remove
        print("The computer picked [", tower[computer_tower_index], "] from the discard pile.", sep='')
        return tower

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
        taken_from_main = get_top_brick(main_pile)
        computer_tower_index = (taken_from_main - 1) // 6
        brick_to_remove = tower[computer_tower_index]
        tower[computer_tower_index] = taken_from_main
        discard.insert(0, brick_to_remove)  # Place new brick and move unwanted brick into discard.
        print("The computer picked [", tower[computer_tower_index], "] from the main pile.", sep='')
        return tower
