
import random
from traceback import print_tb

import sys
sys.stdout = open('output.txt', 'w')

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
            print("Value entered is not correct")
    else:
        print("No choice was recorded...")
except:
    print("You have not made any ticket purchase")


try:
    bread_response=input("Do you want to purchase some bread? Y = YES and N = NO: ")
    if bread_response != "":


        if bread_response == "Y" or bread_response == "y":
            bread_response=int(input("Enter number of loaves: "))
            if bread_response >0:

                total_br_spent = bread_response * br_price
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


try:

    milk_response=input("Do you want to purchase some Milk? Y = YES and N = NO: ")

    if milk_response != "":


        if milk_response == "Y" or milk_response == "y":
            milk_response=int(input("Enter number of milk packets: "))
            if milk_response >0:
                total_mk_spent = milk_response * mk_price
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



try:

    soda_response=input("Do you want to purchase some Sodas? Y = YES and N = NO: ")

    if soda_response == "Y" or soda_response == "y":
        soda_response=int(input("Enter number of sodas: "))
        if soda_response >0:

            total_sd_spent = soda_response * sd_price
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

except:
    print("The value entered is not recognized.")

if in_money>=200:
    try:

        extra_ticket = input("You have some extra balance, Do you want to purchase an extra ticket? Y = YES and N=NO")

        if extra_ticket == "y" or extra_ticket == "Y":
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
            print("No ticket was purchased")
    except:
        print("No extra ticket was purchased")

print("Thank you ",customer_name,",the following is your purchased goods..")
print("Lottery purchased",total_lt_purchased)
print("Bread purchased",bread_response )
print("Milk cartons purchased",milk_response)
print("Soda bottles purchased ",soda_response)

#if bread_response >=2 and milk_response >=1:


print("The total list of expenses is as follows: ")
for pr_name, pr_tt_price in busket.items():
  print(pr_name, pr_tt_price)

print("Total spent: ",total_spent, "and the balance is: ",in_money)


sys.stdout.close()




