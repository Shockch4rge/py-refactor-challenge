from after.classes.cart import Cart


class PaymentProcessor:
    """Responsible for handling payments and validating credentials."""

    def __init__(self, cart: Cart):
        self.cart = cart

    def get_total_price(self) -> float:
        """Calculates the total price of the cart, including GST and discounts."""
        for product in self.cart.products:
            if product.discountable:
                PaymentProcessor.apply_discount(product.price)

            PaymentProcessor.apply_gst(product.price)

        total_price = sum([product.price for product in self.cart.products])
        return total_price

    @staticmethod
    def apply_discount(price: float):
        price *= 0.85

    @staticmethod
    def apply_gst(price: float):
        price *= 1.07
