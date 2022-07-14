
import random
from traceback import print_tb

#import sys
#sys.stdout = open('output.txt', 'w')

lt_price = 200
br_price = 95
mk_price = 70
sd_price = 60

in_money = 400
total_spent=0

total_lt_purchased = 0
total_br_purchased = 0
total_mk_purchased = 0
total_sd_purchased = 0

busket={}


try:
    customer_name = input("Welcome to eSoko, kindly provide your name: ")

except:
    print("Value entered not as expected")


print("Thank you ", customer_name,"We have following products and their prices,\n"
"Lotter tickets @200 each\n"
"Bread @ ksh.95 each\n"
"Milk @ Ksh. 70 per packet\n"
"Soda @ Ksh. 60 per bottle ")

print("You carrently have Ksh. ", in_money)

try:
    ticket_purchase = input("Do you want to purchase a ticket ? Y for yes and N for no. ")

    if ticket_purchase != "":
        if ticket_purchase == "y" or ticket_purchase == "Y":

            total_lt_purchased +=1
            total_spent += 200
            in_money =in_money - lt_price

            lottery_chance = random.randint(0, 2)
            if lottery_chance == 1:
                lottery_no=random.randrange(10, 101)
                total_won =(lottery_no/100)*1000
                in_money = in_money + total_won
                lost = lt_price - total_won
                amount_won = total_won - lt_price
                #in_money = 

                if total_won < lt_price:
                    print("Sorry you lost: ",lost)
                    print("You currently have Ksh. ", in_money)
                else:
                    print("You won ", total_won, "Congratulations", )
                    print("You currently have Ksh. ", in_money)

                busket["Total Tickets"]=total_lt_purchased


            
            else:
                print("Sorry you did get the winning ticket")


            

            
        else:
            print("Value entered is not correct")
    else:
        print("No choice was recorded...")
except:
    print("You have not made any ticket purchase")


try:
    bread_response=input("Do you want to purchase some bread? Y = YES and N = NO: ")
    if bread_response != "":


        if bread_response == "Y" or bread_response == "y":
            total_br_purchased=int(input("Enter number of loaves: "))
            if total_br_purchased >0:

                total_br_spent = total_br_purchased * br_price
                if total_br_spent <= in_money:
                    busket["Bread"]=total_br_spent
                    total_spent += total_br_spent
                    in_money -=total_br_spent
                    print("Busket currently has ",busket)
                    print("Your wallet balance is ",in_money)

                else:
                    print("The total cost is more than your ewallet balance")

    else:
        print("Value entered is not correct")
except:
    print("Ensure value entered is correct as expected")

if in_money >=mk_price:

    try:

        milk_response=input("Do you want to purchase some Milk? Y = YES and N = NO: ")

        if milk_response != "":


            if milk_response == "Y" or milk_response == "y":
                total_mk_purchased=int(input("Enter number of milk packets: "))
                if total_mk_purchased > 0:
                    total_mk_spent = total_mk_purchased * mk_price
                    if total_mk_spent <=in_money:
                        busket["Milk"]=total_mk_spent
                        total_spent += total_mk_spent
                        in_money -=total_mk_spent
                        print(busket)
                        print("Your wallet balance is ",in_money)


                    else:
                        print("The total cost is more than your ewallet balance")

                else:
                    print("The value entered is not correct")

            else:
                print("Value entered is not correct")
        else:
            print("Value entered is not correct")

    except:
        print("Response entered is not recognized")

else:
    print("Not enough to purchase milk")

if in_money >= sd_price:


    try:

        soda_response=input("Do you want to purchase some Sodas? Y = YES and N = NO: ")

        if soda_response == "Y" or soda_response == "y":
            total_sd_purchased=int(input("Enter number of sodas: "))
            if total_sd_purchased >0:

                total_sd_spent = total_sd_purchased * sd_price
                if total_sd_spent <=in_money:
                    busket["Soda"]=total_sd_spent
                    total_spent += total_sd_spent
                    in_money -=total_sd_spent
                    print(busket)
                    print("Your wallet balance is ",in_money)


                else:
                    print("The total cost is more than your ewallet balance")

            else:
                print("Enter a correct Value")
        else:
            print("Response entered was not valid.")
    except:
        print("The value entered is not recognized.")

if in_money>=200:
    try:

        extra_ticket = input("You have some extra balance, Do you want to purchase an extra ticket? Y = YES and N=NO: ")

        if extra_ticket == "y" or extra_ticket == "Y":

            lottery_chance = random.randint(0, 2)
            if lottery_chance == 1:


                lottery_no=random.randrange(20, 101)
                total_won =(lottery_no/100)*1000
                in_money = in_money + total_won
                total_lt_purchased +=1
                busket["Total Tickets"]=total_lt_purchased

                lost = lt_price - total_won
                amount_won = total_won - lt_price
                #in_money = 

                if total_won < lt_price:
                    print("Sorry you lost: ",lost)
                    print("You currently have Ksh. ", in_money)
                else:
                    print("You won ", total_won, "Congratulations", )
                    print("You currently have Ksh. ", in_money)

            else:
                print("Sorry you did not get the winning ticket")
                in_money = in_money - lt_price
            

        else:
            print("No ticket was purchased")
    except:

        print("No extra ticket was purchased")

else:
    print("You do not have enough funds for extra lottery ticket")


if total_br_purchased >=2 and total_mk_purchased >=1:
    bb_promo = random.randint(0,6)
    if bb_promo == 2:
        bb_award = random.randint(50,200)
        in_money = in_money + bb_award

    else:
        print("Keep buying for another chance to win big with blueband")
else:
    print("We have a blueband promotion that works when you purchase 2 loaves bread and a packet of milk")


#Guess the number game at the counter

print("""I have a game for you, am thinking a number between 0 and 20
guess the correct answer and 1 will give you a 50 discount on your total purchase
Remember you only have 3 chances""")

win_number = 4
chances=2
while chances >= 0:
    guess = int(input("Guess a number between o and 20: "))
    if guess >=0 and guess <=20:

        if guess == win_number:
            print("Congratulations, that was a correct guess")
            total_spent = total_spent - (0.5 * total_spent)
            print(total_spent)
            break
        
        elif guess < win_number:
            print(f'The winning number is higher than {guess}, try again, chances remaining: {chances}')
            chances -=1 
        
        elif guess > win_number:
            print(f'The winning number is lower than {guess}, try again, chances remaining: {chances}')
            chances -=1 
    
    else:
        print("Sorry the guess number should be between 0 and 20 strictly")






print("The total list of expenses is as follows: ")
print("Thank you ",customer_name,",the following is your purchased goods..")
print("Lottery purchased",total_lt_purchased)
print("Bread purchased",total_br_purchased )
print("Milk cartons purchased",total_mk_purchased)
print("Soda bottles purchased ",total_sd_purchased)
for pr_name, pr_tt_price in busket.items():

    print(pr_name, pr_tt_price)

    print("Total spent: ",total_spent, "and the balance is: ",in_money)


#sys.stdout.close()




