import sys

from tabulate import tabulate


def main_menu():
    print("------------------------TECH EMPORIUM-------------------------\n")
    print("""Welcome to the Tech Emporium App, how may we assist you today?\n
        1. View your current cart
        2. Check if the item is in your cart   
        3. Add item to your cart
        4. Remove item from your cart
        5. Item count
        6. Clear cart
        7. View our inventory
        8. Proceed to payment
        9. Exit
        """)

    action = input("Please select a number which corresponds with your desired action: ")

    if action == '1':
        show_cart()
    elif action == '2':
        check_for_item()
    elif action == '3':
        add_item()
    elif action == '4':
        remove_item()
    elif action == '5':
        cart_content()
    elif action == '6':
        clear_cart()
    elif action == '7':
        show_inventory()
    elif action == '8':
        check_out()
        return
    elif action == '9':
        calculate_gst_price()
    else:
        print('Please select a valid number from the list given above!')
    main_menu()


cart = []

category_sorting = {
    'CATEGORY': ['LAPTOP', 'LAPTOP', 'LAPTOP', 'TABLET', 'TABLET', 'TABLET', 'GAME CONSOLE', 'GAME CONSOLE',
                 'GAME CONSOLE'],
    'ITEM': ['APPLE MACBOOK AIR', 'ASUS S533EQ 15.6', 'LENOVO IP 3', 'SAMSUNG 64GB GALAXY TAB', 'APPLE 10.2-INCH IPAD',
             'HUAWEI HW-BAH3 LTE', 'NINTENDO SWITCH CONSOLE', 'SONY PLAYSTATION 5', 'MICROSOFT XBOX CONSOLE'],
    'PRICE EXCLUDING GST': ['$1345.00', '$1448.00', '$1308.00', '$372.00', '$456.00', '$372.00', '$457.00', '$560.00',
                            '$653.00'],
    'GST 7%': ['$94.15', '$101.36', '$91.56', '$26.04', '$31.92', '$26.04', '$31.99', '$39.20', '$45.71'],
    'MEMBERSHIP DISCOUNT': ['YES', 'NO', 'NO', 'NO', 'YES', 'YES', 'YES', 'NO', 'YES'],
    'ITEM NUMBER': ['1', '2', '3', '4', '5', '6', '7', '8', '9']
}

ascending_sorting = {
    'CATEGORY': ['TABLET', 'TABLET', 'TABLET', 'GAME CONSOLE', 'GAME CONSOLE', 'GAME CONSOLE', 'LAPTOP', 'LAPTOP',
                 'LAPTOP'],
    'ITEM': ['SAMSUNG 64GB GALAXY TAB', 'HUAWEI HW-BAH3 LTE ', 'APPLE 10.2-INCH IPAD', 'NINTENDO SWITCH CONSOLE',
             'SONY PLAYSTATION 5', 'MICROSOFT XBOX CONSOLE', 'LENOVO IP 3', 'APPLE MACBOOK AIR', 'ASUS S533EQ 15.6'],
    'PRICE EXCLUDING GST': ['$372.00', '$372.00', '$472.00', '$457.00', '$560.00', '$653.00', '$1,308.00', '$1,345.00',
                            '$1,448.00'],
    'GST 7%': ['$26.04', '$26.04', '$31.92', '$31.99', '$39.20', '$47.51', '$91.56', '$94.16', '$101.36'],
    'MEMBERSHIP DISCOUNT': ['NO', 'YES', 'YES', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO'],
    'ITEM NUMBER': ['4', '6', '5', '7', '8', '9', '3', '1', '2']}

alphabetical_sorting = {
    'CATEGORY': ['TABLET', 'LAPTOP', 'LAPTOP', 'TABLET', 'LAPTOP', 'GAME CONSOLE', 'GAME CONSOLE', 'TABLET',
                 'GAME CONSOLE'],
    'ITEM': ['APPLE 10.2-INCH IPAD', 'APPLE MACBOOK AIR', 'ASUS S533EQ 15.6', 'HUAWEI HW-BAH3 LTE', 'LENOVO IP 3',
             'MICROSOFT XBOX CONSOLE', 'NINTENDO SWITCH CONSOLE', 'SAMSUNG 64GB GALAXY TAB', 'SONY PLAYSTATION 5'],
    'PRICE EXCLUDING GST': ['$456.00', '$1,345.00', '$1,448.00', '$372.00', '$1,308.00', '$653.00', '$457.00',
                            '$372.00', '$560.00'],
    'GST 7%': ['$31.92', '$94.15', '$101.36', '$26.04', '$91.56', '$45.71', '$31.99', '$26.04', '$39.20'],
    'MEMBERSHIP DISCOUNT': ['YES', 'YES', 'NO', 'YES', 'NO', 'YES', 'YES', 'NO', 'NO'],
    'ITEM NUMBER': ['5', '1', '2', '6', '3', '9', '7', '4', '8']}

choice_sorting = {'SORT BY': ['CATEGORY', ' ASCENDING PRICE', 'ALPHABETICAL ORDER'], 'ACTION NUMBER': ['1', '2', '3']}

initial_item_price = {
    'APPLE MACBOOK AIR': 1345.00,
    'ASUS S533EQ 15.6': 1448.00,
    'LENOVO IP 3': 1308.00,
    'SAMSUNG 64GB GALAXY TAB': 372.00,
    'APPLE 10.2-INCH IPAD': 456.00,
    'HUAWEI HW-BAH3 LTE': 372.00,
    'NINTENDO SWITCH CONSOLE': 457.00,
    'SONY PLAYSTATION 5': 560.00,
    'MICROSOFT XBOX CONSOLE': 653.00
}

itemsWithDiscount = {
    'APPLE MACBOOK AIR': True,
    'APPLE 10.2-INCH IPAD': True,
    'HUAWEI HW-BAH3 LTE': True,
    'NINTENDO SWITCH CONSOLE': True,
    'MICROSOFT XBOX CONSOLE': True
}


def show_cart():
    print('\n+++++++++++++++++++++++++ITEMS IN YOUR CART+++++++++++++++++++++++++\n')
    if len(cart) == 0:
        print('\nYour cart is empty!\n\n')
    else:
        print(f"* {i}\n" for i in cart)


def check_for_item():
    print(tabulate(category_sorting, headers='keys', tablefmt='fancy_grid'))
    item = input('What item would you like to check? Please copy and paste the name of the item here:  ')

    if item not in cart:
        print(f'\nYou have not added {item} to your cart\n')
        return

    print(f'\nYou have already added {item} to your cart\n')


def add_item():
    print(tabulate(choice_sorting, headers='keys', tablefmt='fancy_grid'))
    sorting_choice_index = input('How would you like to view our inventory? Please input an action number: ')
    if sorting_choice_index == '1':
        print(tabulate(category_sorting, headers='keys', tablefmt='fancy_grid'))
    elif sorting_choice_index == '2':
        print(tabulate(ascending_sorting, headers='keys', tablefmt='fancy_grid'))
    elif sorting_choice_index == '3':
        print(tabulate(alphabetical_sorting, headers='keys', tablefmt='fancy_grid'))
    else:
        print('Please select a valid number from the list given above!')

    item_choice_index = int(input('What item would you like to add to your cart? Please input the number provided: '))

    if item_choice_index == 1:
        cart_item = 'APPLE MACBOOK AIR'
    elif item_choice_index == 2:
        cart_item = 'ASUS S533EQ 15.6'
    elif item_choice_index == 3:
        cart_item = 'LENOVO IP 3'
    elif item_choice_index == 4:
        cart_item = 'SAMSUNG 64GB GALAXY TAB'
    elif item_choice_index == 5:
        cart_item = 'APPLE 10.2-INCH IPAD'
    elif item_choice_index == 6:
        cart_item = 'HUAWEI HW-BAH3 LTE'
    elif item_choice_index == 7:
        cart_item = 'NINTENDO SWITCH CONSOLE'
    elif item_choice_index == 8:
        cart_item = 'SONY PLAYSTATION 5'
    elif item_choice_index == 9:
        cart_item = 'MICROSOFT XBOX CONSOLE'
    else:
        cart_item = ""
        print('\nPlease input a valid item number !\n')

    units = int(input('How many units would you like? Enter number: '))

    while not count_total_added(cart_item, units):
        units = int(input("Please input a valid number: "))
    print('\nYou have added ' + str(units) + ' ' + cart_item + ' to your cart\n')


def remove_item():
    print(tabulate(choice_sorting, headers='keys', tablefmt='fancy_grid'))
    sort = input('How would you like to view our inventory? Please input an action number: ')
    if sort == '1':
        print(tabulate(category_sorting, headers='keys', tablefmt='fancy_grid'))
    elif sort == '2':
        print(tabulate(ascending_sorting, headers='keys', tablefmt='fancy_grid'))
    elif sort == '3':
        print(tabulate(alphabetical_sorting, headers='keys', tablefmt='fancy_grid'))
    else:
        print('Please select a valid number from the list given above!')

    user_input = input('What item would you like to remove from your cart? Please input the number provided: ')

    if user_input == '1':
        cart_item = 'APPLE MACBOOK AIR'
    elif user_input == '2':
        cart_item = 'ASUS S533EQ 15.6'
    elif user_input == '3':
        cart_item = 'LENOVO IP 3'
    elif user_input == '4':
        cart_item = 'SAMSUNG 64GB GALAXY TAB'
    elif user_input == '5':
        cart_item = 'APPLE 10.2-INCH IPAD'
    elif user_input == '6':
        cart_item = 'HUAWEI HW-BAH3 LTE'
    elif user_input == '7':
        cart_item = 'NINTENDO SWITCH CONSOLE'
    elif user_input == '8':
        cart_item = 'SONY PLAYSTATION 5'
    elif user_input == '9':
        cart_item = 'MICROSOFT XBOX CONSOLE'
    else:
        while True:
            print('\nPlease input a valid item number!\n')

    units = int(input('How many units would you like to remove? Enter number: '))

    while not count_total_removed(cart_item, units):
        units = int(input("Please input a valid number: "))
    print('\nYou have removed ' + str(units) + ' ' + cart_item + ' to your cart\n')


def cart_content():
    print('\nThere are', len(cart), 'items in the cart\n')


def clear_cart():
    cart.clear()
    print('\nYour cart has been cleared\n')


def show_inventory():
    print(tabulate(choice_sorting, headers='keys', tablefmt='fancy_grid'))
    sort = input('How would you like to view our inventory? Please input an action number: ')
    if sort == '1':
        print(tabulate(category_sorting, headers='keys', tablefmt='fancy_grid'))
    elif sort == '2':
        print(tabulate(ascending_sorting, headers='keys', tablefmt='fancy_grid'))
    elif sort == '3':
        print(tabulate(alphabetical_sorting, headers='keys', tablefmt='fancy_grid'))
    else:
        print('Please select a valid number from the list given above!')


def count_total_added(name, amount):
    if amount == 1:
        return name, amount

    if amount > 1:
        for i in range(amount):
            cart.append(name)

    return cart


def count_total_removed(itemName, itemAmount):
    for i in range(itemAmount):
        cart.remove(itemName)


def check_out():
    if len(cart) == 0:
        print('\nYour cart is empty!\n\n')
    else:
        payment_choice = input('Would you like to proceed with payment? (y/n): ')

        if payment_choice.lower() == 'y':
            proceed_to_payment()
        elif payment_choice.lower() == 'n':
            main_menu()
        else:
            print('Please input either y or n.')
            check_out()


def proceed_to_payment():
    calculate_gst_price()
    check_for_discount_card()


def check_for_discount_card():
    if input('Do you have a Discount Card? (y/n): ').lower() == 'y':
        check_card_number(input('Please enter your Discount Card Number: '))
    else:
        pass


def check_card_number(number):
    if len(number) == 5:
        if number[0].lower() == 'd' and number[4].lower() == 'c':
            print('Your Discount Card is valid!')
        else:
            print('Your Discount Card is invalid!')
    else:
        proceed_to_payment()


def calculate_gst_price():
    print('Calculating price inclusive of GST.')
    print(sum(initial_item_price[i] * 1.07 for i in cart))


def apply_discount():
    print('Congratulations, you are entitled to a discount!')


main_menu()
