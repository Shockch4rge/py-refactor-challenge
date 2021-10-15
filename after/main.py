import sys
from enum import Enum

from after.classes.cart import Cart


class Action(Enum):
    CART_SHOW = "1"
    CART_CHECK_PRODUCT = "2"
    CART_ADD_PRODUCT = "3"
    CART_REMOVE_PRODUCT = "4"
    CART_CLEAR = "5"
    MENU_SHOW = "6"
    PAY = "7"
    EXIT = "8"


def print_menu():
    print("\n------------------------TECH EMPORIUM-------------------------\n")
    print(
        """
        Welcome to the Tech Emporium App, how may we assist you today?\n
        1. View your current cart
        2. Add item to your cart
        3. Remove item from your cart
        4. Check if the item is in your cart   
        5. Clear cart
        6. View our inventory
        7. Proceed to payment
        8. Exit
        """
    )


def read_action() -> str:
    return input("Please select a number which corresponds with your desired action: ")


def main():
    """Create an empty cart."""
    cart = Cart()

    print_menu()
    action = read_action()

    # Show cart
    if action == Action.CART_SHOW:
        cart.show()

    # Check for product
    elif action == Action.CART_CHECK_PRODUCT:
        product_name = input("What item would you like to check? Please copy and paste the name of the item here: ")
        cart.check_product_in_cart(product_name)

    # Add product
    elif action == Action.CART_ADD_PRODUCT:
        product_name = input("What item would you like to add? Please specify the item (case sensitive): ")
        cart.add(product_name)

    # Remove product
    elif action == Action.CART_REMOVE_PRODUCT:
        product_name = input("What item would you like to remove? Please specify the item name (case sensitive): ")
        cart.remove(product_name)

    # Clear cart
    elif action == Action.CART_CLEAR:
        cart.clear()

    # Show inventory
    elif action == Action.MENU_SHOW:
        pass

    # Pay
    elif action == Action.PAY:
        pass

    # Exit
    elif action == Action.EXIT:
        print("Thank you for shopping with us!")
        sys.exit()

    else:
        print('Please select a valid number from the list given above!')


if __name__ == '__main__':
    main()
