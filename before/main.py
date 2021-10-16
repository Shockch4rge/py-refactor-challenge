import sys  # This imports the sys.exit() function used.
from tabulate import tabulate  # This imports the package which formats all my tables.


def mainMenu():  # This function prints the main menu.
    print('---------------------------TECH EMPORIUM----------------------------\n')
    print('''Welcome to the Tech Emporium App. How may we assist you today?\n
        1. View our inventory
        2. Add an item to your cart
        3. Remove item from your cart
        4. Clear your cart
        5. Item count
        6. Check if an item is in your cart
        7. View your cart
        8. Proceed to payment
        9. Exit
        ''')
    action = input(
        'Please select a number which corresponds with your desired action: ')  # User chooses their action by entering the corresponding number.
    if action == '7':
        showCart()
    elif action == '6':
        checkItem()
    elif action == '2':
        addItem()
    elif action == '3':
        removeItem()
    elif action == '5':
        listLength()
    elif action == '4':
        clearCart()
    elif action == '1':
        showInventory()
    elif action == '8':
        checkOut()
    elif action == '9':
        sys.exit()
    else:
        print('Please select a valid number from the list given above!')
    mainMenu()  # This calls the functions that prints the main menu.


itemPricesInitial = {'APPLE MACBOOK AIR': 1345.00,
                     # This dictionary stores the prices of each item before GST and 15%, making it effectively the brain of majority of the code.
                     'ASUS S533EQ 15.6': 1448.00,
                     'LENOVO IP 3': 1308.00,
                     'SAMSUNG 64GB GALAXY TAB': 372.00,
                     'APPLE 10.2-INCH IPAD': 456.00,
                     'HUAWEI HW-BAH3 LTE': 372.00,
                     'NINTENDO SWITCH CONSOLE': 457.00,
                     'SONY PLAYSTATION 5': 560.00,
                     'MICROSOFT XBOX CONSOLE': 653.00}

itemPricesDiscount = {'APPLE MACBOOK AIR': 1439.15,
                      # This dictionary stores the prices of the items which are to be discounted. Prices are after GST. Those with a value of '0' have no discount.
                      'ASUS S533EQ 15.6': 0,
                      'LENOVO IP 3': 0,
                      'SAMSUNG 64GB GALAXY TAB': 0,
                      'APPLE 10.2-INCH IPAD': 487.92,
                      'HUAWEI HW-BAH3 LTE': 398.04,
                      'NINTENDO SWITCH CONSOLE': 488.99,
                      'SONY PLAYSTATION 5': 0,
                      'MICROSOFT XBOX CONSOLE': 698.71}

cart = []  # This list stores all the items that the user adds to the cart.

# The following dictionaries are what my tabulate() function uses to make tables. It uses the dictionary keys as headers.
# This dictionary sorts the shop's inventory by category
sortCategory = {'CATEGORY': ['LAPTOP', 'LAPTOP', 'LAPTOP', 'TABLET', 'TABLET', 'TABLET', 'GAME CONSOLE', 'GAME CONSOLE',
                             'GAME CONSOLE', 'MAIN MENU'],
                'ITEM': ['APPLE MACBOOK AIR', 'ASUS S533EQ 15.6', 'LENOVO IP 3', 'SAMSUNG 64GB GALAXY TAB',
                         'APPLE 10.2-INCH IPAD', 'HUAWEI HW-BAH3 LTE', 'NINTENDO SWITCH CONSOLE', 'SONY PLAYSTATION 5',
                         'MICROSOFT XBOX CONSOLE'],
                'PRICE EXCLUDING GST': ['$1345.00', '$1448.00', '$1308.00', '$372.00', '$456.00', '$372.00', '$457.00',
                                        '$560.00', '$653.00'],
                'GST 7%': ['$94.15', '$101.36', '$91.56', '$26.04', '$31.92', '$26.04', '$31.99', '$39.20', '$45.71'],
                'MEMBERSHIP DISCOUNT': ['YES', 'NO', 'NO', 'NO', 'YES', 'YES', 'YES', 'NO', 'YES'],
                'ITEM NUMBER': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']}
# This dictionary sorts the shop's inventory by ascending price.
sortAscending = {
    'CATEGORY': ['TABLET', 'TABLET', 'TABLET', 'GAME CONSOLE', 'GAME CONSOLE', 'GAME CONSOLE', 'LAPTOP', 'LAPTOP',
                 'LAPTOP', 'MAIN MENU'],
    'ITEM': ['SAMSUNG 64GB GALAXY TAB', 'HUAWEI HW-BAH3 LTE ', 'APPLE 10.2-INCH IPAD', 'NINTENDO SWITCH CONSOLE',
             'SONY PLAYSTATION 5', 'MICROSOFT XBOX CONSOLE', 'LENOVO IP 3', 'APPLE MACBOOK AIR', 'ASUS S533EQ 15.6'],
    'PRICE EXCLUDING GST': ['$372.00', '$372.00', '$472.00', '$457.00', '$560.00', '$653.00', '$1,308.00', '$1,345.00',
                            '$1,448.00'],
    'GST 7%': ['$26.04', '$26.04', '$31.92', '$31.99', '$39.20', '$47.51', '$91.56', '$94.16', '$101.36'],
    'MEMBERSHIP DISCOUNT': ['NO', 'YES', 'YES', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO'],
    'ITEM NUMBER': ['4', '6', '5', '7', '8', '9', '3', '1', '2', '10']}
# This dictionary sorts the shop's inventory by descending price.
sortDescending = {
    'CATEGORY': ['LAPTOP', 'LAPTOP', 'LAPTOP', 'GAME CONSOLE', 'GAME CONSOLE', 'GAME CONSOLE', 'TABLET', 'TABLET',
                 'TABLET', 'MAIN MENU'],
    'ITEM': ['ASUS S533EQ 15.6', 'APPLE MACBOOK AIR', 'LENOVO IP 3', 'MICROSOFT XBOX CONSOLE', 'SONY PLAYSTATION 5',
             'NINTENDO SWITCH CONSOLE', 'APPLE 10.2-INCH IPAD', 'SAMSUNG 64GB GALAXY TAB', 'HUAWEI HW-BAH3 LTE'],
    'PRICE EXCLUDING GST': ['$1,448.00', '$1,345.00', '$1,308.00', '$653.00', '$560.00', '$457.00', '$456.00',
                            '$372.00', '$372.00'],
    'GST 7%': ['$101.36', '$94.15', '$91.56', '$45.71', '$39.20', '$31.99', '$31.92', '$26.04', '$26.04'],
    'MEMBERSHIP DISCOUNT': ['NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'YES', 'NO', 'YES'],
    'ITEM NUMBER': ['2', '1', '3', '9', '8', '7', '5', '4', '6', '10']}
# This dictionary sorts the shop's inventory by alphabetical order.
sortAlphabetical = {
    'CATEGORY': ['TABLET', 'LAPTOP', 'LAPTOP', 'TABLET', 'LAPTOP', 'GAME CONSOLE', 'GAME CONSOLE', 'TABLET',
                 'GAME CONSOLE', 'MAIN MENU'],
    'ITEM': ['APPLE 10.2-INCH IPAD', 'APPLE MACBOOK AIR', 'ASUS S533EQ 15.6', 'HUAWEI HW-BAH3 LTE', 'LENOVO IP 3',
             'MICROSOFT XBOX CONSOLE', 'NINTENDO SWITCH CONSOLE', 'SAMSUNG 64GB GALAXY TAB', 'SONY PLAYSTATION 5'],
    'PRICE EXCLUDING GST': ['$456.00', '$1,345.00', '$1,448.00', '$372.00', '$1,308.00', '$653.00', '$457.00',
                            '$372.00', '$560.00'],
    'GST 7%': ['$31.92', '$94.15', '$101.36', '$26.04', '$91.56', '$45.71', '$31.99', '$26.04', '$39.20'],
    'MEMBERSHIP DISCOUNT': ['YES', 'YES', 'NO', 'YES', 'NO', 'YES', 'YES', 'NO', 'NO'],
    'ITEM NUMBER': ['5', '1', '2', '6', '3', '9', '7', '4', '8', '10']}
# This dictionary stores the data that is used with the sort() function.
sortChoice = {'SORT BY': ['CATEGORY', ' ASCENDING PRICE', 'DESCENDING PRICE', 'ALPHABETICAL ORDER', 'MAIN MENU'],
              'ACTION NUMBER': ['1', '2', '3', '4', '5']}


def showCart():  # This function shows the user their cart.
    print('\n+++++++++++++++++++++++++ITEMS IN YOUR CART+++++++++++++++++++++++++\n')
    if len(cart) == 0:
        print('\nYour cart is empty!\n\n')  # If the cart is empty, it displays this message.
    else:
        itemsInCart()
    returnToMenu()


def checkItem():  # This function checks whether the user has added an item to cart yet.
    print('\n++++++++++++++++++++++++++++ITEM CHECKER++++++++++++++++++++++++++++\n')
    if len(cart) == 0:
        print('\nYour cart is empty!\n\n')  # If the cart is empty, it displays this message.
    else:
        print(tabulate(sortCategory, headers='keys', tablefmt='fancy_grid'))
        # The shop inventory is showed, the user will then copy and paste the name of the item which they wish to check.
        item = input('\nWhat item would you like to check? Please copy and paste the name of the item here: ')
        if item in cart:
            print('\nYou have already added, ' + item + ' to your cart\n')
        else:
            print('\nYou have not added, ' + item + ' to your cart\n')
    returnToMenu()


cartItem = ''  # This assists the addItem() function.


def itemsInCart():
    for cartItem in cart:
        print('*', (cartItem))


def addItem():  # This function allows the user to add items to their cart. It also gives them the opportunity to adjust the quantity of items which they would like to add.
    print(tabulate(sortChoice, headers='keys', tablefmt='fancy_grid'))
    sort = input(
        '\nHow would you like to view our inventory? Please input an action number: ')  # User enters the number that corresponds with how they want the inventory list to be sorted.
    if sort == '1':
        print(tabulate(sortCategory, headers='keys', tablefmt='fancy_grid'))
    elif sort == '2':
        print(tabulate(sortAscending, headers='keys', tablefmt='fancy_grid'))
    elif sort == '3':
        print(tabulate(sortDescending, headers='keys', tablefmt='fancy_grid'))
    elif sort == '4':
        print(tabulate(sortAlphabetical, headers='keys', tablefmt='fancy_grid'))
    elif sort == '5':
        returnToMenu()
    else:
        print('\nPlease select a valid number from the list given above!\n')
        addItem()
    item = input(
        '\nWhat item would you like to add to your cart? Please input the number provided: ')  # User enters reference number of the item they want to add.
    if item == '1':
        cartItem = 'APPLE MACBOOK AIR'
    elif item == '2':
        cartItem = 'ASUS S533EQ 15.6'
    elif item == '3':
        cartItem = 'LENOVO IP 3'
    elif item == '4':
        cartItem = 'SAMSUNG 64GB GALAXY TAB'
    elif item == '5':
        cartItem = 'APPLE 10.2-INCH IPAD'
    elif item == '6':
        cartItem = 'HUAWEI HW-BAH3 LTE'
    elif item == '7':
        cartItem = 'NINTENDO SWITCH CONSOLE'
    elif item == '8':
        cartItem = 'SONY PLAYSTATION 5'
    elif item == '9':
        cartItem = 'MICROSOFT XBOX CONSOLE'
    elif item == '10':
        returnToMenu()
    else:
        print('\nPlease input a valid item number !\n')
        addItem()
    units = int(input(
        '\nHow many units would you like? Enter numeric value: '))  # User enters the quantity of the selected item they want to add.
    while units < 1:
        units = int(input('\nPlease input a value more than 0: '))
    while not calculateQuantityAdd(cartItem, units):
        units = int(input('\nPlease input a valid number: '))
    print('\nYou have added ' + str(units) + ' ' + cartItem + ' to your cart\n')
    askAdd()


def askAdd():  # This function asks the user if they want to add more items to their cart.
    askIfAddAnother = input('Would you like to add more items (y/n) :')
    if askIfAddAnother.lower() == 'y':
        addItem()
    elif askIfAddAnother.lower() == 'n':
        returnToMenu()
    else:
        print('\nPlease choose (y/n)\n')
        askAdd()


def removeItem():  # This function allows users to remove items from their cart. They are also able to remove any quantity of the selected item.
    if len(cart) == 0:
        print('\n\nYour cart is empty!\n\n')  # If the cart is empty, it displays this message.
    else:
        print(tabulate(sortChoice, headers='keys', tablefmt='fancy_grid'))
        sort = input(
            '\nHow would you like to view our inventory? Please input an action number: ')  # User enters the number that corresponds with how they want the inventory list to be sorted.
        if sort == '1':
            print(tabulate(sortCategory, headers='keys', tablefmt='fancy_grid'))
        elif sort == '2':
            print(tabulate(sortAscending, headers='keys', tablefmt='fancy_grid'))
        elif sort == '3':
            print(tabulate(sortDescending, headers='keys', tablefmt='fancy_grid'))
        elif sort == '4':
            print(tabulate(sortAlphabetical, headers='keys', tablefmt='fancy_grid'))
        elif sort == '5':
            returnToMenu()
        else:
            print('Please select a valid number from the list given above!')
            removeItem()
        item = input(
            '\nWhat item would you like to remove from your cart? Please input the number provided: ')  # User enters the reference number of the item they want to remove.
        if item == '1':
            cartItem = 'APPLE MACBOOK AIR'
            if cartItem not in cart:
                print()
                print(cartItem, 'is not in your cart!\n')
                removeItem()
        elif item == '2':
            cartItem = 'ASUS S533EQ 15.6'
            if cartItem not in cart:
                print()
                print(cartItem, 'is not in your cart!\n')
                removeItem()
        elif item == '3':
            cartItem = 'LENOVO IP 3'
            if cartItem not in cart:
                print()
                print(cartItem, 'is not in your cart!\n')
                removeItem()
        elif item == '4':
            cartItem = 'SAMSUNG 64GB GALAXY TAB'
            if cartItem not in cart:
                print()
                print(cartItem, 'is not in your cart!\n')
                removeItem()
        elif item == '5':
            cartItem = 'APPLE 10.2-INCH IPAD'
            if cartItem not in cart:
                print()
                print(cartItem, 'is not in your cart!\n')
                removeItem()
        elif item == '6':
            cartItem = 'HUAWEI HW-BAH3 LTE'
            if cartItem not in cart:
                print()
                print(cartItem, 'is not in your cart!\n')
                removeItem()
        elif item == '7':
            cartItem = 'NINTENDO SWITCH CONSOLE'
            if cartItem not in cart:
                print()
                print(cartItem, 'is not in your cart!\n')
                removeItem()
        elif item == '8':
            cartItem = 'SONY PLAYSTATION 5'
            if cartItem not in cart:
                print()
                print(cartItem, 'is not in your cart!\n')
                removeItem()
        elif item == '9':
            cartItem = 'MICROSOFT XBOX CONSOLE'
            if cartItem not in cart:
                print()
                print(cartItem, 'is not in your cart!\n')
                removeItem()
        elif item == '10':
            returnToMenu()
        else:
            print('Please input a valid number!')
            removeItem()
        units = int(input(
            '\nHow many units would you like to remove? Enter number: '))  # User enters the quantity of the selected item which they want to remove.
        while units < 1:
            units = int(input('\nPlease input a value more than 0: '))
        while not calculateQuantityRemove(cartItem, units):
            units = int(input('\nPlease input a valid number: '))
        print('\nYou have removed ' + str(units) + ' ' + cartItem + ' to your cart\n')
        askRemove()
    returnToMenu()


def askRemove():  # This function asks the user if they want to remove more items from their cart.
    askIfRemoveAnother = input('Would you like to remove more items (y/n) :')
    if askIfRemoveAnother.lower() == 'y':
        removeItem()
    elif askIfRemoveAnother.lower() == 'n':
        returnToMenu()
    else:
        print('\nPlease choose (y/n)\n')
        askRemove()


def listLength():  # This function displays the amount of items in cart.
    if len(cart) == 0:
        print('\n\nYour cart is empty!\n\n')  # If the cart is empty, it displays this message.
    else:
        print('\nThere are', len(cart), 'items in the cart\n')  # Displays the amount of items in the user's cart.
    returnToMenu()


def clearCart():  # This function clears the user's cart.
    if len(cart) == 0:
        print('\n\nYour cart is empty!\n\n')  # If the cart is empty, it displays this message.
    else:
        print('\n Your cart has been cleared!')
        cart.clear()
        returnToMenu()


def showInventory():  # This function allows the user to view the shop's inventory.
    print(tabulate(sortChoice, headers='keys', tablefmt='fancy_grid'))
    sort = input(
        '\nHow would you like to view our inventory? Please input an action number: ')  # User enters the number that corresponds with how they want the inventory list to be sorted.
    if sort == '1':
        print(tabulate(sortCategory, headers='keys', tablefmt='fancy_grid'))
        returnToMenu()
    elif sort == '2':
        print(tabulate(sortAscending, headers='keys', tablefmt='fancy_grid'))
        returnToMenu()
    elif sort == '3':
        print(tabulate(sortDescending, headers='keys', tablefmt='fancy_grid'))
        returnToMenu()
    elif sort == '4':
        print(tabulate(sortAlphabetical, headers='keys', tablefmt='fancy_grid'))
        returnToMenu()
    elif sort == '5':
        returnToMenu()
    else:
        print('Please select a valid number from the list given above!')
        showInventory()


def checkOut():  # This function starts the payment process.
    if len(cart) == 0:
        print('\n\nYour cart is empty!\n\n')  # If the cart is empty, it displays this message.
        returnToMenu()
    else:
        print('\n+++++++++++++++++++++++++ITEMS IN YOUR CART+++++++++++++++++++++++++\n')  # Shows the user their cart.
        for cartItem in cart:
            print('* ' + cartItem)
        paymentChoice = input(
            '\nWould you like to proceed with payment? (y/n): ')  # User chooses if they want to proceed with payment.
        if paymentChoice.lower() == 'y':
            proceedPayment()
        elif paymentChoice.lower() == 'n':
            returnToMenu()
        else:
            print('\nPlease input either y or n.\n')


def returnToMenu():  # This function prompts the user to press 'enter' to return to the main menu.
    returnMenu = input('\nPress enter to return to main menu: ')
    if returnMenu == '':
        mainMenu()


def calculateQuantityAdd(itemName,
                         itemAmount):  # This function adds multiple units of any selected item to the user's cart.
    if itemAmount == 0:
        return True
    elif itemAmount > 0:
        for i in range(itemAmount):
            cart.append(itemName)
            i += 1
        return True
    else:
        return False


def calculateQuantityRemove(itemName,
                            itemAmount):  # This function removes multiple units of any selected item from the user's cart.
    if int(itemAmount) == 0:
        return True
    elif int(itemAmount) > 0:
        for i in range(itemAmount):
            cart.remove(itemName)
            i += 1
        return True
    else:
        return False


def proceedPayment():  # This function starts the payment process.
    calculateGSTPrice()
    discountCard()


def discountCardNumberCheck(userInput):  # This function checks the validity of the user's Discount Card.
    if len(userInput) == 5 and userInput[0].lower() == 'd':
        print(
            '\nYour Discount Card is valid!')  # A valid Discount Card has a string length of 5 and a always starts with a 'd'.
        applyDiscount()
    else:
        print('\nYour Discount Card is invalid!')
        proceedPayment()


def discountCard():  # This function asks if the user has a Discount Card.
    hasCard = input(
        '\nDo you have a Discount Card? (y/n): ')  # User enters 'y' or 'n', depending on whether they have a Discount Card.
    if hasCard.lower() == 'y':
        discountCardNumberCheck(input('\nPlease enter your Discount Card Number: '))
    elif hasCard.lower() == 'n':
        finalPriceWithoutDiscount()
    else:
        proceedPayment()  # If no valid input is detected, it re-runs the payment process.


def calculateGSTPrice():  # This function calculates the prices of each item after GST and adds them together.
    print('\nCalculating price inclusive of GST...')
    print('\nYour bill inclusive of GST is $', round(sum(itemPricesInitial[i] * 1.07 for i in cart), 2))


def applyDiscount():  # This function calculates the 15% discount if the user's discount card is valid.
    discountPrices = sum(itemPricesDiscount[i] * 0.15 for i in
                         cart)  # This equation calculates the amount of discount the user receives.
    if discountPrices == 0:
        print(
            '\nSorry, none of the items in your cart were discountable.')  # This message is displayed if the user has a valid discount card but none of the items in their card are part of the discount list.
        finalPriceWithoutDiscount()
    else:
        print('\nCongratulations, you are entitled to a discount on selected items!')
        print('\nYou have received a total discount of: $', round(sum(itemPricesDiscount[i] * 0.15 for i in cart),
                                                                  2))  # Displays the amount of discount the user receives.
        print('\nYour final total is: $',
              round(finalPriceWithDiscount(), 2))  # Displays the final amount of money the user has to pay.
        continueShopping = input(
            '\nThank you for shopping with Tech Emporium! Would you like to exit? (y/n): ')  # Gives user a choice to either exit or return to main menu.
        if continueShopping.lower() == 'y':
            sys.exit()
        elif continueShopping.lower() == 'n':
            cart.clear()
            returnToMenu()
        else:
            print('Please enter (y/n)!')
            applyDiscount()


def finalPriceWithoutDiscount():  # This function is called if the user does not have a discount card.
    print('\nPlease pay $', round(sum(itemPricesInitial[i] * 1.07 for i in cart),
                                  2))  # Displays the final amount of money the user has to pay.
    continueShopping = input(
        '\nThank you for shopping with Tech Emporium! Would you like to exit? (y/n): ')  # Gives user a choice to either exit or return to main menu.
    if continueShopping.lower() == 'y':
        sys.exit()
    elif continueShopping.lower() == 'n':
        cart.clear()
        returnToMenu()
    else:
        print('Please enter (y/n)!')
        finalPriceWithoutDiscount()


def finalPriceWithDiscount():  # This function subtracts the total discount from the price with GST before discount.
    priceWithGST = sum(itemPricesInitial[i] * 1.07 for i in cart)
    totalDiscount = sum(itemPricesDiscount[i] * 0.15 for i in cart)
    final = priceWithGST - totalDiscount
    return final


mainMenu()
