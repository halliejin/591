
# import the random module
import random

# use "winnings = random.randint(2, 10)" to generate a random int from 2 - 10 and store in a variable "winnings"

# unit price of a lottery ticket
constant_lottery_unit_price = 2

# unit price of an apple
constant_apple_unit_price = .99

# unit price of a can of beans
constant_canned_beans_unit_price = 1.58

# unit price of a soda
constant_soda_unit_price = 1.23

# the user has initial $5 for shopping
money = 5

# the user has spent $0 initially
money_spent = 0

# the amounts of lottery tickets, apples, cans of beans, and sodas the user has purchased
lottery_amount, apple_amount, canned_beans_amount, soda_amount = 0, 0, 0, 0

# print the welcome message and product list
print("Welcome to the supermarket!  Here's what we have in stock:\n"
      "- Lottery tickets cost $2 each\n"
      "- Apples cost $0.99 each\n"
      "- Cans of beans cost $1.58 each\n"
      "- Sodas cost $1.23 each\n")
# print the money available
print("You have ${} available".format(money))

# decision for a lottery
decision = input("First, do you want to buy a $2 lottery ticket for a chance at winning $2-$10? (y/n)")

# the customer chooses to buy the lottery
if decision == ("y" or "Y"):
    lottery_count = 1
    # generate the probability
    probability = random.randint(0, 2)

    # simulate the winning case and set the probability to 33%
    if probability <= 2 * 0.33:
        winnings = random.randint(2, 10)
        print("Congrats! You won ${}!\n".format(winnings))
        money += winnings - 2
    # simulate the losing case
    else:
        winnings = 0
        print("Sorry! You did not win the lottery.\n")
        money -= 2

# the customer chooses not to buy the lottery
else:
    lottery_count = 0
    winnings = 0
    print("No lottery tickets were purchased.\n")

# print the money available after the decision for lottery
print("You have ${} available".format(money))

# decision for apples
apple = input("Do you want to buy apple(s)? (y/n)")

# the customer chooses to buy apples
if apple == ("y" or "Y"):
    apple_count = input("How many apple(s) do you want to buy?")

    # using exception handling to record the apples bought
    try:
        # type casting from str to int
        apple_count = int(apple_count)

        # count the expense for apples
        apple_expense = apple_count * constant_apple_unit_price

        # add a constraint if the money is insufficient
        if apple_expense > money:
            print("Not enough money.\n")
            apple_count = 0

        # print to the console with purchasing information
        else:
            print("The user wants to buy {} apple(s). This will cost ${}.".format(apple_count, apple_expense))
            print("The user has enough money. {} apple(s) purchased.\n".format(apple_count))
            money -= apple_expense
    # warning for invalid inputs
    except ValueError as e:
        print("Integer values only! No apples selected.\n")
        apple_count = 0

# the customer chooses not to buy apples
else:
    apple_count = 0
    print("No apples purchased.\n")


# similar structure as apples
# decision for beans
bean = input("Do you want to buy can(s) of beans? (y/n)")

# the customer chooses to buy cans of beans
if bean == ("y" or "Y"):
    bean_count = input("How many can(s) of beans do you want to buy?")

    try:
        bean_count = int(bean_count)
        bean_expense = bean_count * constant_canned_beans_unit_price
        if bean_expense > money:
            print("Not enough money.\n")
            bean_count = 0
        else:
            print("The user wants to buy {} can(s) of beans. This will cost ${}.".format(bean_count, bean_expense))
            print("The user has enough money. {} can(s) of beans purchased.\n".format(bean_count))
            money -= bean_expense

    except ValueError as e:
        print("Integer values only! No apples selected.\n")
        bean_count = 0

# the customer chooses not to buy cans of beans
else:
    bean_count = 0
    print("No can(s) of beans purchased.\n")


# similar structure as apples
# decision for sodas
sodas = input("Do you want to buy soda(s)?(y/n)")
if sodas == ("y" or "Y"):
    sodas_count = input("How many soda(s) do you want to buy?")

    try:
        sodas_count = int(sodas_count)
        sodas_expense = sodas_count * constant_soda_unit_price
        if sodas_expense > money:
            print("Not enough money.\n")
            sodas_count = 0
        else:
            print("The user wants to buy {} soda(s). This will cost ${}.".format(bean_count, sodas_expense))
            print("The user has enough money. {} soda(s) purchased.\n".format(sodas_count))
            money -= sodas_expense
    except ValueError as e:
        print("Integer values only! No apples selected.\n")
        sodas_count = 0

else:
    sodas_count = 0
    print("No sodas purchased.\n")

# print the information when shopping is over
print("Money left: ${}\n"
      "Lottery ticket(s) purchased: {}\n"
      "Lottery winnings: ${}\n"
      "Apple(s) purchased: {}\n"
      "Can(s) of beans purchased: {}\n"
      "Soda(s) purchased: {}\n"
      "Good bye!".format(money, lottery_count, winnings, apple_count, bean_count, sodas_count))

