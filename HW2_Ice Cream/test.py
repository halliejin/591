#
# def print_welcome_and_menu(list_of_flavors, list_of_sizes, list_of_prices):
#     """
#     Prints the following:
#     1. Welcome message (Must contain word 'welcome')
#     2. Message on what flavors are available in the ice cream store.
#         Hint: Loop through the list_of_flavors
#     3. Message on how much each size cost.
#         Hint: Loop through the list_of_sizes, list_of_prices
#         Format should be: Our {size} ice cream is ${price}.
#     """
#     # TODO: Write your code here
#     print("Welcome to Penn's Student Run Ice Cream Stand!\n")
#     print("Our current flavors for today are:\n")
#
#     i = 0
#     for f in list_of_flavors:
#         print(f)
#
#     while (i < len(list_of_sizes)):
#         for p in list_of_prices:
#             print("Our {} ice cream is: {}".format(list_of_sizes[i],p))
#             i += 1
#
# list1 = ["Cho", "Vin", "Str"]
# list2 = ["s", "m", "l"]
# list3 = ['1', '2', '3']
#
# print_welcome_and_menu(list1,list2,list3)


# def get_order_qty(customer_name):
#     """
#     Ask the customer how many orders of ice cream they want.
#     Valid order quantity should be an integer 1-5 inclusive. If outside the range or non-int, re-prompt.
#     Hint: When asking for user input, cast it to an integer. If the input cannot be cast-ed to an integer, re-prompt.
#     If the input is a float, Example: 2.54 will return 2 and follow the rules of string to integer casting.
#     Returns: How many orders of ice cream the customer wants.
#     """
#     order_qty = 0
#     # TODO: Write your code here
#
#     while True:
#         try:
#             order = input("How many ice creams will you be ordering (1 to 5)?")
#             order_qty = int(float(order))
#             if 1 <= order_qty <= 5:
#                 break
#             else:
#                 continue
#         except ValueError:
#             print("Please enter a valid integer")
#             continue
#
#     return order_qty
#
# get_order_qty("Judy")

# string1 = "   \n\t\r   \nvinalla"
# print(string1.strip())

# string2 = input("say sth: \n").strip()
# print(string2)
#
# string2 = string2.replace("\\n", "")
#
# string2 = string2.replace("\\t", "")
# string2 = string2.replace("\\r", "")
# string2 = string2.replace("\\f", "")
# string2 = string2.strip()
# print(string2)
#


def get_first_letter_of_user_input(question):
    """
    Takes in a string as its argument, to be used as the question you want the user to be asked.
    Gets input from the user, removes whitespace and makes all letters lowercase
    Hint: Use the strip() and lower() functions
    Returns: The first letter of the input the user provides. Ask again if the input is empty.
    """

    first_letter = ""
    # TODO: Write your code here

    while first_letter == "":
        user_input = ""
        while user_input == "":
            user_input = input(question).strip()
            user_input = user_input.strip()
            if user_input != "":
                first_letter = user_input.lower()[0]
                return first_letter
            else:
                break

print(get_first_letter_of_user_input("question"))